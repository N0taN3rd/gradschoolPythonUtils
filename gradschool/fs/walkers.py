from pathlib import Path
from collections import deque

from ..fn import T


def list_dir(dirpath='.', filterfn=None):
    """
    Lists the contents of a directory with the ability to optionally filter the directory's contents.
    :param dirpath: Path to the directory to be listed. Defaults to current working directory
    :param filterfn: Optional filter function. If supplied only the items
    within the director that this function returns true for will be yielded
    :return: Generator yielding the contents of the directory as pathlib.Path objects
    """
    if dirpath is None:
        raise ValueError('Must supply a path to a directory to list')
    dp = Path(dirpath)
    if filterfn is not None:
        return list_dirf(dirpath, filterfn)
    for item in dp.iterdir():
        yield item


def list_dirf(dirpath='.', filterfn=T):
    """
    Lists the contents of a directory using a filtering function.
    If no filtering functions are supplied all directories and files are yielded
    :param dirpath: Path to the directory to be listed. Defaults to current working directory
    :param filterfn: A filtering function that returns true for the items that will be yielded
    :return: Generator yielding the contents of the directory as pathlib.Path objects
    """
    if dirpath is None:
        raise ValueError('Must supply a path to a directory to list')
    if filterfn is None:
        raise ValueError('Must supply a filtering function')
    dp = Path(dirpath)
    for item in dp.iterdir():
        if filterfn(item):
            yield item


def rlist_dir(dirpath='.', ffilter=None, dfilter=None):
    """
    Lists the contents of a directory recursively with
    the ability to optionally supply a file and or directory filtering function.
    If no filtering functions are supplied all directories and files are yielded
    Uses a deque internally. All directories are appended right and popped left.
    :param dirpath: Path to the directory to be listed. Defaults to current working directory
    :param ffilter: Optional file filtering function. If supplied only the files contained within all visited
    directories that the function returns true for will be yielded
    :param dfilter: Optional directory filtering function. If supplied only the directories
    within the initial directory the function returns true for will be visited
    :return: Generator yielding the contents of the directory and child directories as pathlib.Path objects
    """
    if dirpath is None:
        raise ValueError(
            'Must supply a path to a directory to recursively list')
    if ffilter is not None or dfilter is not None:
        return rlist_dirf(dirpath, ffilter=ffilter, dfilter=dfilter)
    q = deque([Path(dirpath)])
    while q:
        cur = q.popleft()
        for item in cur.iterdir():
            yield item
            if item.is_dir():
                q.append(item)


def rlist_dirf(dirpath='.', ffilter=T, dfilter=T):
    """
    Lists the contents of a directory recursively with
    the ability to supply a file and or directory filtering function.
    If no filtering functions are supplied all directories and files are yielded.
    Uses a deque internally. All directories are appended right and popped left
    :param dirpath: Path to the directory to be listed. Defaults to current working directory
    :param ffilter: File filtering function, only the files contained within all visited
    directories that the function returns true for will be yielded
    :param dfilter: Directory filtering function, only the directories
    within the initial directory the function returns true for will be visited
    :return: Generator yielding the contents of the directory and child directories as pathlib.Path objects
    """
    if dirpath is None:
        raise ValueError(
            'Must supply a path to a directory to recursively list')
    if ffilter is None:
        ffilter = T
    if dfilter is None:
        dfilter = T
    q = deque([Path(dirpath)])
    while q:
        cur = q.popleft()
        for item in cur.iterdir():
            if ffilter(item):
                yield item
            if item.is_dir() and dfilter(item):
                q.append(item)
