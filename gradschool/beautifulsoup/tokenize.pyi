from typing import Callable, Generator, List, Tuple, Optional, Union

from nltk.tokenize import TweetTokenizer
from nltk.tokenize.api import TokenizerI


class SoupTokenizer(object):
    htmlfp: str
    tokenizer: Union[str, TweetTokenizer, TokenizerI]
    preprocess: Callable[[str], str]
    parser: str

    def __init__(self,
                 htmlfp: str,
                 tokenizer: Union[str, TweetTokenizer, TokenizerI],
                 preprocess: Optional[Callable[[str], str]] = None,
                 parser: str = 'lxml'): pass

    def __enter__(self) -> List[str]: pass


def multi_soup_tokenize(
        htmlfiles: List[str],
        tokenizer: Union[str, TweetTokenizer, TokenizerI],
        preprocess: Optional[Callable[[str], str]] = None,
        parser: str = 'lxml') -> Generator[Tuple[str, List[str]]]: pass
