__license__ = "MIT"

from bs4 import BeautifulSoup


class SoupFromFile(object):
    """
    Utility class to simplify the process of reading HTML files using BeautifulSoup

    Example:
        with SoupFromFile('example.html') as soup:
           for tag in soup.find_all(True):
               print(tag.name)
    """

    def __init__(self, htmlfp, parser='lxml'):
        """
        :param htmlfp: Path to html file to get some soup from
        :param parser: The html parser to use. Defaults to lxml
        """
        if htmlfp is None:
            raise ValueError('The htmlfp argument was None')
        self.file_obj = open(htmlfp, 'r')
        self.parser = parser

    def __enter__(self):
        return BeautifulSoup(self.file_obj.read(), self.parser)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


class SoupSaver(object):
    """
    Utility class to simplify the process of reading and manipulating HTML files using BeautifulSoup

    Example:
        with SoupSaver('example.html', htmlsp='modifiedExample.html') as soup:
           for tag in soup.find_all(True):
               if tag.name == 'a':
                   tag.string = 'New Link text.'
    """

    def __init__(self, htmlfp, htmlsp=None, parser='lxml',
                 pretty=False, formatter=None):
        """
        :param htmlfp: Path to html file to get some soup from
        :param htmlsp: Path to file containing the manipulated html contained in htmlfp.
        Defaults to htmlfp.
        :param parser: The html parser to use. Defaults to lxml
        :param pretty: Pretty print the html to be saved. Defaults to false
        :param formatter: Optional formatter for pretty printing.
        See the BeautifulSoup documentation for more information.
        """
        if htmlfp is None:
            raise ValueError('The htmlfp argument was None')
        self.htmlsp = htmlsp if htmlsp is not None else htmlfp
        self.file_obj = open(htmlfp, 'r')
        self.parser = parser
        self.pretty = pretty
        self.formatter = formatter
        self.soup = None

    def __enter__(self):
        self.soup = BeautifulSoup(self.file_obj.read(), self.parser)
        return self.soup

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        with open(self.htmlsp, 'w') as out:
            if self.pretty:
                htmls = self.soup.prettify(formatter=self.formatter)
            else:
                htmls = str(self.soup)
            out.write(htmls)


def multi_soup_reader(htmlfiles, parser='lxml'):
    """
    Get the BeautifulSoup for multiple HTMLs files
    :param htmlfiles: List of HTML file paths to be read
    :param parser: The html parser to use. Defaults to lxml
    :return: Returns a generator that yields filename, soup
    """
    if htmlfiles is None or not htmlfiles:
        raise ValueError('The htmlfiles argument is None or empty')
    for htmlfile in htmlfiles:
        with SoupFromFile(htmlfile, parser=parser) as soup:
            yield htmlfile, soup


def multi_soup_saver(htmlfiles, parser='lxml', pretty=False, formatter=None):
    """
    Read, modify and save multiple HTML files using BeautifulSoup
    :param htmlfiles: List of tuples (htmlfile, savepath) or htmlfile, to read and modify.
    If a list of strings is supplied the the original file is overrriden
    :param parser: The html parser to use. Defaults to lxml
    :param pretty: Pretty print the html to be saved. Defaults to false
    :param formatter: Optional formatter for pretty printing.
    :return: Returns a generator that yields htmlfile, soup
    """
    if htmlfiles is None or len(htmlfiles) == 0:
        raise ValueError('The htmlfiles argument is None or empty')
    for rs in htmlfiles:
        if isinstance(rs, tuple):
            htmlfp, htmlsp = rs
        else:
            htmlfp = htmlsp = rs
        with SoupSaver(htmlfp, htmlsp=htmlsp, parser=parser, pretty=pretty, formatter=formatter) as soup:
            yield htmlfp, soup
