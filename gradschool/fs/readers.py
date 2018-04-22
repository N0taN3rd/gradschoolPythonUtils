import csv
import os
from collections import deque
from functools import partial

from ..fn import identity
from .savers import AutoSaver

try:
    import ujson as json
except ImportError:
    import json


def stripline(line, stripboth=False):
    """
    Default line transformer.
    Returns the supplied line after calling rstrip
    :param line: string representing a file line
    :param stripboth: Optional boolean flag indicating both l and r strip should be applied
    :return: The trimmed line
    """
    if stripboth:
        return line.lstrip().rstrip()
    return line.rstrip()


def tail(filep, n=10):
    """
    Returns the last n lines of file
    :param filep: Path to the file
    :param n: How many lines to keeps. Defaults to 10
    :return: list containing the last n lines
    """
    with open(filep) as f:
        return list(deque(f, maxlen=n))


def read_plaintext(textfilep, mapper=None):
    """
    Reads a plain text file line by line
    :param textfilep: Path to text file
    :param mapper: Optional function to be applied to each line of file
    :return: Generator yield each line of the file
    """
    with open(os.path.expanduser(textfilep), 'r') as textin:
        if mapper is not None:
            for line in textin:
                yield mapper(line)
        else:
            for line in textin:
                yield line


class CSVFile(object):
    """
    Utility class for reading csv files.

    Example:
        with CSVFile('example.csv') as csvfile:
            for row in csvfile:
                print(row)
    """

    def __init__(self, csv_path, fieldnames=None, restkey=None,
                 restval=None, dialect='excel', *args, **kwds):
        """
        :param csv_path: Path to csv file to be read
        :param fieldnames: Optional list of fieldnames
        :param restkey: Optional key name for the remaining data in a row that are not in fieldnames
        :param restval: Optional key name for the keys of fieldnames not found in a row
        :param dialect: Optional csv data format
        """
        self.csvin = open(os.path.expanduser(csv_path), 'r')
        self.reader = csv.DictReader(
            self.csvin,
            fieldnames=fieldnames,
            restkey=restkey,
            restval=restval,
            dialect=dialect,
            *args,
            **kwds)

    def __enter__(self):
        """
        :return: The csv.DictReader for the csv file
        """
        return self.reader

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.csvin.close()


def read_csv(csv_path, fieldnames=None, restkey=None,
             restval=None, dialect='excel', *args, **kwds):
    """
    Read the contents of a csv file
    :param csv_path: Path to csv file to be read
    :param fieldnames: Optional list of fieldnames
    :param restkey: Optional key name for the remaining data in a row that are not in fieldnames
    :param restval: Optional key name for the keys of fieldnames not found in a row
    :param dialect: Optional csv data format
    :return: csv.DictReader
    """
    with CSVFile(os.path.expanduser(csv_path), fieldnames=fieldnames, restkey=restkey, restval=restval,
                 dialect=dialect, *args, **kwds) as csvfile:
        return csvfile


class JsonFile(object):
    """
    Utility class for reading json files.

    Example:
       with JsonFile('example.json') as jsonfile:
           print(jsonfile)
    """

    def __init__(self, jsonfp):
        """
        :param jsonfp: Path to json file
        """
        self.jsonin = open(jsonfp, 'r')

    def __enter__(self):
        """
        :return: The contents of the json file
        """
        return json.load(self.jsonin)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.jsonin.close()


def read_json(jsonfp):
    """
    Returns the contents of a json file
    :param str jsonfp: Path to json file
    """
    with JsonFile(jsonfp) as jsondata:
        return jsondata


class FilePrinter(object):
    """
    Utility context class for printing the contents of a file
    """

    def __init__(self, file_p, line_transformer=partial(
            stripline, stripboth=True)):
        """
        :param file_p: Path to file to be printed
        :param line_transformer: Optional function to transform the file's lines before printing.
        Defaults to stripline
        """
        self.file_obj = open(file_p, 'r')
        self.line_transformer = line_transformer

    def __enter__(self):
        for line in self.file_obj:
            print(self.line_transformer(line))
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


class SelectFromFile(object):
    """
    Utility context class that yields a generator that will apply a transformation and selector function
    to each line of the file.
    If the selector or transformer functions return none the line is skipped otherwise the line is yielded
    """

    def __init__(self, filep, selector=identity,
                 transformer=partial(stripline, stripboth=True)):
        """
        :param filep: Path to file to select lines from
        :param selector: Optional selector function. Defaults to fn.identity
        :param transformer: Optional line transformer function. Defaults to stripline
        """
        self.file_obj = open(filep, 'r')
        self.line_transformer = transformer
        self.selector = selector

    def _do_selection(self):
        """
        :return: Generator yielding the transformed and selected lines from the file
        """
        for line in self.file_obj:
            toyield = self.line_transformer(line)
            if toyield is not None:
                selected = self.selector(toyield)
                if selected is not None:
                    yield selected

    def __enter__(self):
        return self._do_selection()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


class CleanFile(object):
    """
    Utility context class that will sanitize the lines of a file using the supplied mapper and sorting functions,
    with the option to save the sanitized lines back to the same or different file.

    Example:
        with CleanFile('example.txt', mapfn=lamda x: x.rstrip()) as flines:
            for line in flines:
                print(line)
    """

    def __init__(self, filep, saveto=None, save_back=False,
                 mapfn=identity, sortfn=identity):
        """
        :param filep: Path to file to be cleaned
        :param saveto: Optional path to file the clean contents of the file at filep will be saved to.
        Defaults to filep if save_back is True.
        :param save_back: Optional boolean flag indicating the clean lines should be save back to a file
        :param mapfn: String returning function applied to each line of file. Defaults to fn.identity
        :param sortfn: Function returning the lines of the file at filep in sorted order. Defaults to fn.identity
        """
        if filep is None:
            raise ValueError(
                'The path to the file to be read was not supplied')
        self.file_p = filep
        self.save_p = saveto if saveto is not None else filep
        self.file_obj = open(filep, 'r')
        self.mapfn = mapfn
        self.clean_lines = []
        self.save_back = save_back
        self.sort_output = sortfn

    def __enter__(self):
        for line in self.sort_output(self.file_obj):
            self.clean_lines.append(self.mapfn(line))
        return self.clean_lines

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        if self.save_back:
            with AutoSaver(self.save_p, accu=list) as out:
                out.extend(self.clean_lines)
