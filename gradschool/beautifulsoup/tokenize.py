from .readsave import SoupFromFile
from .util import get_tokenizer


class SoupTokenizer(object):
    """
    Applies the supplied tokenizer class from nltk.tokenize to the text of an HTML file.
    Also applies an additional function to the text of the HTML file if supplied.

    Example:
        with SoupTokenizer('example.html', tokenizer=WordPunctTokenizer) as tokens:
            for token in tokens:
                print(tokens)
    """

    def __init__(self, htmlfp, tokenizer, preprocess=None, parser='lxml'):
        """
        :param htmlfp: Path to html file to get some soup from
        :param tokenizer: nltk.tokenize class, class instance,
        or class name string to use
        :param preprocess: Additional but optional function to be
        applied to the text of the HTML File
        :param parser: The html parser to use. Defaults to lxml
        """
        if htmlfp is None:
            raise ValueError('The htmlfp argument is None')
        if tokenizer is None:
            raise ValueError('The tokenizer argument is None')
        self.htmlfp = htmlfp
        self.tokenizer = get_tokenizer(tokenizer)
        self.preprocess = preprocess
        self.parser = parser

    def __enter__(self):
        """
        :return: List of tokens
        """
        with SoupFromFile(self.htmlfp, parser=self.parser) as soup:
            if self.preprocess is not None:
                text = self.preprocess(soup.text)
            else:
                text = soup.text
        return self.tokenizer.tokenize(text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def multi_soup_tokenize(htmlfiles, tokenizer, preprocess=None, parser='lxml'):
    """
    Applies the supplied tokenizer class from nltk.tokenize to the text of an multiple HTML files.
    Also applies an additional function to the text of a HTML file if supplied.

    Example:
      for name, tokens in multi_soup_tokenize(['html1.html', 'html2.html'], tokenizer=WordPunctTokenizer):
          print('%s has these tokens' % name)
          for token in tokens:
              print(token)

    :param htmlfiles: List of html file paths to get some tokenized soup from
    :param tokenizer: nltk.tokenize class, class instance,
    or class name string to use
    :param preprocess: Additional but optional function to be
    applied to the text of the HTML File
    :param parser: The html parser to use. Defaults to lxml
    :return: Generator yielding a tuple containing
    the file name and the list of tokens contained in the file.
    One tuple per file in the list of html files
    """
    if htmlfiles is None or not htmlfiles:
        raise ValueError('The htmlfiles argument is None or empty')
    if tokenizer is None:
        raise ValueError('The tokenizer argument is None')
    toke = get_tokenizer(tokenizer)
    for htmlfile in htmlfiles:
        with SoupFromFile(htmlfile, parser=parser) as soup:
            if preprocess is not None:
                text = preprocess(soup.text)
            else:
                text = soup.text
            yield htmlfile, toke.tokenize(text)
