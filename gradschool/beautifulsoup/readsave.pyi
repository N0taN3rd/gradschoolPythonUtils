from typing import Callable, Generator, List, TextIO, Tuple, Optional, Union

from bs4 import BeautifulSoup


class SoupFromFile(object):
    file_obj: TextIO
    parser: str

    def __init__(self, htmlfp: str, parser: str = 'lxml'): pass

    def __enter__(self) -> BeautifulSoup: pass


class SoupSaver(object):
    htmlfp: str
    htmlsp: Optional[str]
    file_obj: TextIO
    parser: str
    pretty: bool
    formatter: Optional[Union[str, Callable]]
    soup: BeautifulSoup

    def __init__(self,
                 htmlfp: str,
                 htmlsp: Optional[str] = None,
                 parser: str = 'lxml',
                 pretty: bool = False,
                 formatter: Optional[Union[str, Callable]] = None): pass

    def __enter__(self) -> BeautifulSoup: pass


def multi_soup_reader(
        htmlfiles: List[str],
        parser: str = 'lxml') -> Generator[Tuple[str, BeautifulSoup]]: pass


def multi_soup_saver(
        htmlfiles: List[Union[str, Tuple[str, str]]],
        parser: str = 'lxml',
        pretty: bool = False,
        formatter: Optional[Union[str, Callable]] = None) -> Generator[Tuple[str, BeautifulSoup]]: pass
