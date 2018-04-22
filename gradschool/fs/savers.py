# -*- coding: utf-8 -*-

import csv
from contextlib import contextmanager

try:
    import ujson as json
except ImportError:
    import json

from tabulate import tabulate

from .formatters import default_formatter, format_output


def get_accumulator(accu):
    """
    Initializes the accumulator.
    If it is callable, type reference, calls the constructor.
    Otherwise returns the accumulator.
    :param accu: The data accumulator
    :return: The initialized accumulator
    """
    if callable(accu):
        return accu()
    return accu


def selected_data(accu, selector):
    """
    Returns the selected data.
    If the selector function is not None, returns the results of
    applying the selector function to accu.
    Otherwise returns accu.
    :param accu: The data accumulator
    :param selector: Optional iterable returning function that has the items to be saved
    :return:
    """
    if selector is None:
        return accu
    return selector(accu)


@contextmanager
def auto_saver(filepath, accu=list, formatter=default_formatter,
               selector=None):
    """
    Function version of the class autosavers.AutoSaver
    :param filepath: Path to file to be created with the contents of accu
    :param accu: The data accumulator, i.e. list, dict, your type, etc. Defaults to list
    :param formatter: String returning function that will format the data to be saved to filepath
    :param selector: Optional iterable returning function that has the items to be saved to filepath
    :return:
    """
    if filepath is None:
        raise ValueError('The file argument was not supplied')

    to_serialize = get_accumulator(accu)

    yield to_serialize

    outl = selected_data(to_serialize, selector)

    with open(filepath, 'w') as out:
        for it in outl:
            out.write(format_output(it, formatter))


@contextmanager
def auto_save2(filep1, filep2, accu1=list, accu2=list,
               formater1=default_formatter,
               formater2=default_formatter,
               selector1=None, selector2=None):
    """
    Function version of the class autosavers.AutoSaveTwo
    :param filep1: Path to file to be created with the contents of accu1
    :param filep2: Path to file to be created with the contents of accu2
    :param accu1: The data accumulator for filep1, i.e. list, dict, your type, etc. Defaults to list
    :param accu2: The data accumulator for filep2, i.e. list, dict, your type, etc. Defaults to list
    :param formater1: String returning function that will format the data to be saved to filep1
    :param formater2: String returning function that will format the data to be saved to filep2
    :param selector1: Optional iterable returning function that has the items to be saved to filep1
    :param selector2: Optional iterable returning function that has the items to be saved to filep2
    :return: Tuple of accu1, accu2
    """
    if filep1 is None and filep2 is None:
        raise ValueError(
            'Both file path arguments, fp1 and fp2, were not supplied')
    elif filep1 is None:
        raise ValueError('The file argument fp1 was not supplied')
    elif filep2 is None:
        raise ValueError('The file argument fp2 was not supplied')

    to_serialize1 = get_accumulator(accu1)
    to_serialize2 = get_accumulator(accu2)

    yield to_serialize1, to_serialize2

    outl = selected_data(to_serialize1, selector1)
    with open(filep1, 'w') as out:
        for it in outl:
            out.write(format_output(it, formater1))

    outl2 = selected_data(to_serialize2, selector2)
    with open(filep2, 'w') as out:
        for it in outl2:
            out.write(format_output(it, formater2))


@contextmanager
def auto_csv(file, fieldnames):
    """
    Function version of the class autosavers.AutoSaveCsv
    :param file: Path to csv file to be created
    :param fieldnames: List of column names
    :return: accumulator (list) to put data in
    """
    accu = list()
    yield accu
    with open(file, 'w') as out:
        writer = csv.DictWriter(out, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(accu)


@contextmanager
def auto_latextbl(file, headers, accu=list):
    """
    Function version of the class autosavers.AutoSLatexTable
    :param file: Path to latex table file to be created
    :param headers: The table headers.
    Please consult https://pypi.org/project/tabulate for the list off header
    options and formats. The value for this argument is dependant on accu
    and its format.
    :param accu: The data accumulator that is a list or dict. Defaults to list
    :return: accumulator to put data in
    """
    serialize = get_accumulator(accu)
    yield serialize
    with open(file, 'w') as out:
        out.write(
            tabulate(serialize, headers=headers, tablefmt='latex')
        )


class AutoSaver(object):
    """
    Utility context class that will save the contents of stype to a file.
    Customization of the format for each item to be saved is done through formatter.
    Customization/Selection of the items to be saved to file is done by selector.
    """

    def __init__(self, file, accu=list,
                 formatter=default_formatter,
                 selector=None):
        """
        :param file: Path to file to be created with the contents of save_type
        :type file: str
        :param accu: The data holder, i.e. list, dict, etc. Defaults to list
        :param formatter: String returning function that will format the data to be saved to file
        Defaults to default_formatter
        :param selector: Optional iterable returning function that has the items to be saved to file
        """
        if file is None:
            raise ValueError('The file argument was not supplied')
        self.file = file
        self.accumulator = get_accumulator(accu)
        self.formatter = formatter
        self.selector = selector

    def __enter__(self):
        """
        :return: The accumulator
        """
        return self.accumulator

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.selector is None:
            outl = self.accumulator
        else:
            outl = self.selector(self.accumulator)
        with open(self.file, 'w') as out:
            for it in outl:
                formatted = self.formatter(it)
                if not formatted.endswith('\n'):
                    formatted = formatted + '\n'
                out.write(formatted)


class AutoSaveTwo(object):
    """
    Utility context class that uses two of the AutoSaver classes in this module
    For more information see each the documentation of the AutoSaver classes in this module
    """

    def __init__(self, autos1, autos1_args, autos2, autos2_args):
        """
        :param autos1: Class reference to autosaver 1
        :param autos1_args: Dictionary of arguments supplied to autosaver 1
        :param autos2: Class reference to autosaver 2
        :param autos2_args: Dictionary of arguments supplied to autosaver 2
        """
        self.f = autos1(**autos1_args)
        self.s = autos2(**autos2_args)

    def __enter__(self):
        return self.f.__enter__(), self.s.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.__exit__(exc_type, exc_val, exc_tb)
        self.s.__exit__(exc_type, exc_val, exc_tb)


class AutoSaveCsv(object):
    """
    Utility context class for csv.DictWriter.
    """

    def __init__(self, file, fieldnames):
        """
        :param file: Path to csv file to be created
        :param fieldnames: List of column names
        """
        if file is None:
            raise ValueError('The file argument was not supplied')
        self.accu = list()
        self.file = file
        self.fieldnames = fieldnames

    def __enter__(self):
        """
        :return: accumulator to put data in
        :rtype: list
        """
        return self.accu

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file, 'w') as out:
            writer = csv.DictWriter(out, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.accu)


class AutoSaveJson(object):
    """
    Utility context class for saving data as json.
    """

    def __init__(self, file, accu=list):
        """
        :param file: Path to json file to be created
        :param accu: Data accumulator. Defaults to list
        """
        if file is None:
            raise ValueError('The file argument was not supplied')
        self.accu = get_accumulator(accu)
        self.file = file

    def __enter__(self):
        """
        :return: accumulator to put data in
        """
        return self.accu

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file, 'w') as out:
            out.write(json.dumps(self.accu))


class AutoSLatexTable(object):
    """
    Utility context class for tabulate.tabulate.
    """

    def __init__(self, file, headers, accu=list):
        """
        :param file: Path to latex table file to be created
        :param headers: List of table headers
        """
        self.accu = get_accumulator(accu)
        self.file = file
        self.headers = headers

    def __enter__(self):
        """
        :return: The data accumulator
        """
        return self.accu

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file, 'w') as out:
            out.write(
                tabulate(self.accu, headers=self.headers, tablefmt='latex')
            )
