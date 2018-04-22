from urllib.parse import urlparse, parse_qs, urlsplit, urljoin, quote as uquote, quote_plus as uquote_plus, \
    unquote as uunquote, unquote_plus as uunquote_plus, urlencode

import tldextract
from goldfinch import validFileName as vfn


def is_absolute(url):
    """
    Tests if a URL is absolute
    :param url: URL to test
    :return: True if absolute otherwise false
    """
    return bool(urlparse(url).netloc)


def is_relative(url):
    """
    Tests if a URL is relative
    :param url: URL to test
    :return: True if relative otherwise false
    """
    return not is_absolute(url)


def split(url, scheme='', allow_fragments=True):
    """Wrapper for urllib.parse.urlsplit"""
    return urlsplit(url, scheme=scheme, allow_fragments=allow_fragments)


def join(base, url, allow_fragments=True):
    """Wrapper for urllib.parse.urljoin"""
    return urljoin(base, url, allow_fragments=allow_fragments)


def parse(url, scheme='', allow_fragments=True):
    """Wrapper for urllib.parse.urlparse"""
    return urlparse(url, scheme='', allow_fragments=True)


def parse_query(qs, keep_blank_values=False, strict_parsing=False,
                encoding='utf-8', errors='replace'):
    """Wrapper for urllib.parse.parse_query"""
    return parse_qs(qs, keep_blank_values=keep_blank_values, strict_parsing=strict_parsing, encoding=encoding,
                    errors=errors)


def quote(url, safe='/', encoding=None, errors=None):
    """Wrapper for urllib.parse.quote"""
    return uquote(url, safe=safe, encoding=encoding, errors=errors)


def quote_plus(url, safe='/', encoding=None, errors=None):
    """Wrapper for urllib.parse.quote_plus"""
    return uquote_plus(url, safe=safe, encoding=encoding, errors=errors)


def unquote(url, encoding='utf-8', errors='replace'):
    """Wrapper for urllib.parse.unquote"""
    return uunquote(url, encoding=encoding, errors=errors)


def unquote_plus(url, encoding='utf-8', errors='replace'):
    """Wrapper for urllib.parse.unquote_plus"""
    return uunquote_plus(url, encoding=encoding, errors=errors)


def encode(query, doseq=False, safe='', encoding=None,
           errors=None, quote_via=quote_plus):
    """Wrapper for urllib.parse.encode"""
    return urlencode(query, doseq=doseq, safe=safe,
                     encoding=encoding, errors=errors, quote_via=quote_via)


def extract_url(url):
    """Wrapper for teldextract"""
    return tldextract.extract(url)


def extract_domain(url):
    """Uses teldextract to retrieve the domain of the url"""
    return tldextract.extract(url).domain


def extract_regdomain(url):
    """Uses teldextract to retrieve the registered_domain of the url"""
    return tldextract.extract(url).registered_domain


def extract_subdomain(url):
    """Uses teldextract to retrieve the subdomain of the url"""
    return tldextract.extract(url).subdomain


def extract_suffix(url):
    """Uses teldextract to retrieve the suffix of the url"""
    return tldextract.extract(url).suffix


def filenamify(url, rcolslash='_', space='underscore',
               initCap=True, ascii=True):
    """
    Filenamifies a URL using goldfish
    :param url:  The URL to filenamify
    :param rcolslash: Replacement string for removing "://" and "/"
    :param space:  'underscore', 'remove',or 'keep'
    :param initCap: True or False
    :param ascii:  True or False
    :return: The filenamified URL
    """
    return vfn(url.replace('://', rcolslash).replace('/', rcolslash), space=space, initCap=initCap, ascii=ascii).decode(
        "utf-8")
