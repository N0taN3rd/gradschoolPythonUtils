from typing import Any, Generic, Union, overload

from nltk.tokenize import TweetTokenizer
from nltk.tokenize.api import TokenizerI


def import_clazz(name: str) -> Any: pass


@overload
def import_clazz(name: str) -> Union[TweetTokenizer, TokenizerI]: pass


def get_tokenizer(tokenizer: str) -> Union[TweetTokenizer, TokenizerI]: pass


@overload
def get_tokenizer(tokenizer: Generic[TokenizerI]) -> TokenizerI: pass


@overload
def get_tokenizer(tokenizer: TweetTokenizer) -> TweetTokenizer: pass
