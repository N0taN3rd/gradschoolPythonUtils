def default_formatter(item):
    """
    Default formatter (%s)
    :param item: The item to save to file
    :return: The item to be saved to file with a newline appended
    """
    return '%s\n' % item


def int_formatter(i):
    """
    Int formatter (%d)
    :param i: The integer to format
    :return: The string representation of i to be saved to file with a newline appended
    """
    return '%d\n' % i


def formatter_str(formatstr):
    """
    Creates a formatter function from format string, i.e. '%s, %s' etc
    :param formatstr: The formatting string
    :return: Formatter function using formatstr
    """
    return lambda item: formatstr % item


def custom_formatter(selector, formatstr):
    """
    Creates a formatter based on applying the function selector on the
    item to be stringified and then interpolates the results using formatstr
    :selector: Function returns the values to be interpolated using formatstr
    :param formatstr: The formatting string , i.e. '%s, %s' etc
    """
    return lambda item: formatstr % selector(item)


def format_output(tosave, formatter):
    """
    Applies the formatting function, formatter, on tosave.
    If the resulting string does not have a newline adds it.
    Otherwise returns the formatted string
    :param tosave: The item to be string serialized
    :param formatter: The formatter function applied to item
    :return: The formatted string after formatter has been applied to tosave
    """
    formatted = formatter(tosave)
    if not formatted.endswith('\n'):
        formatted = formatted + '\n'
    return formatted
