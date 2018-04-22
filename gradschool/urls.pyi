from typing import Any, Dict, Optional, Callable, NamedTuple

from urllib.parse import ParseResult, SplitResult

ExtractResult = NamedTuple(
    'NamedTuple', [
        ('subdomain', str), ('domain', str), ('suffix', str)])


def is_absolute(url: str) -> bool: pass


def is_relative(url: str) -> bool: pass


def split(
    url: str,
    scheme: str = '',
    allow_fragments: bool = True) -> SplitResult: pass


def join(base: str, url: str, allow_fragments: bool = True) -> str: pass


def parse(
    url: str,
    scheme: str = '',
    allow_fragments: bool = True) -> ParseResult: pass


def parse_query(qs: str,
                keep_blank_values: bool = False,
                strict_parsing: bool = False,
                encoding: str = 'utf-8',
                errors: str = 'replace') -> Dict[str, Any]: pass


def quote(url: str,
          safe: str = '/',
          encoding: Optional[str] = None,
          errors: Optional[str] = None) -> str: pass


def quote_plus(url: str,
               safe: str = '/',
               encoding: Optional[str] = None,
               errors: Optional[str] = None) -> str: pass


def unquote(url: str, encoding: str = 'utf-8',
            errors: str = 'replace') -> str: pass


def unquote_plus(url: str, encoding: str = 'utf-8',
                 errors: str = 'replace') -> str: pass


def encode(query: str,
           doseq: bool = False,
           safe: str = '',
           encoding: Optional[str] = None,
           errors: Optional[str] = None,
           quote_via: Callable[..., str] = quote_plus) -> str: pass


def extract_url(url: str) -> ExtractResult: pass


def extract_domain(url: str) -> str: pass


def extract_regdomain(url: str) -> str: pass


def extract_subdomain(url: str) -> str: pass


def extract_suffix(url: str) -> str: pass


def filenamify(url: str,
               rcolslash: str = '_',
               space: str = 'underscore',
               initCap: bool = True,
               ascii: bool = True) -> str: pass
