import os
import pathlib


def as_uri(path):
    """
    Converts the supplied path to file URI
    :param path: Path to be converted
    :return: Path as a fille URI
    """
    p = pathlib.Path(path)
    return p.as_uri()


def as_pathlib(path):
    """
    Converts the supplied path to an pathlib.Path object
    :param path: The path to convert
    :return: The path converted to pathlib.Path
    """
    return pathlib.Path(path)


def isfile(path):
    """
    Determines if the supplied path is a file
    :param path: Path to check
    :return: True if it is a file, False otherwise
    """
    return os.path.isfile(path)


def isdir(path):
    """
    Determines if the supplied path is a directory
    :param path: Path to check
    :return: True if it is a directory, False otherwise
    """
    return os.path.isdir(path)


def is_absolute(path):
    """
    Checks if the supplied path is an absolute path
    :param path: Path to check
    :return: True if absolute path, false, otherwise
    """
    p = pathlib.Path(path)
    return p.is_absolute()


def join_with_cwd(path):
    """
    Joins the supplied path the current working directory
    :param path: Path to be joined with the current working directory
    :return: Path joined with the current working directory
    """
    return os.path.join(os.getcwd(), path)


def basename(path):
    """
    Get the base name of the supplied path
    :param path: Path to get the base name from
    :return: The base name of the path
    """
    return os.path.basename(path)


def dirname(path):
    """
    Get the directory name of the supplied path
    :param path: A path
    :return: The directory name of the path
    """
    return os.path.dirname(path)


def rename(pfrom, pto):
    """
    Renames a file or directory (pfrom) to a new name (pto)
    :param pfrom: Path to file or directory to be renamed
    :param pto: New name or path with new name
    """
    os.rename(pfrom, pto)


def samefile(path1, path2):
    """
    Determines if two paths point to the same file or directory
    :param path1: First path
    :param path2: Second path
    :return: True if same, false otherwise
    """
    return os.path.samefile(path1, path2)


def path_exists(path):
    """
    Tests if a path exists
    :param path: Path to test existence of
    :return: True if path exists or false if it does not
    """
    return os.path.exists(path)


def relpath(path, start=os.curdir):
    """
    Get a relative filepath to path from either current working directory or optional starting point
    :param path: The path to get a relative file path from
    :param start: Optional starting point defaults to os.curdir
    :return: The relative filepath
    """
    return os.path.relpath(path, start=start)


def resolve(path):
    """
    Resolves the supplied path
    :param path: Path to be resolved
    :return: The resolved path
    """
    p = pathlib.Path(path)
    return str(p.resolve())
