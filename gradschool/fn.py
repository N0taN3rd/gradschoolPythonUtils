from collections import defaultdict
from functools import reduce, lru_cache


def identity(x):
    """
    Identity function.
    :param x: Any value
    :return: The same value
    """
    return x


def flatmap(iterable, mapfn):
    """
    Applies a function that can produce an iterable collection of values or a single value
    to each item in the iterable collection.
    Returns a flat list of values produced by mapfn.
    :param iterable: The iterable to have mapfn applied to each of its values
    :param mapfn: The mapping function that produces a single value or an iterable of a many values
    :return: A flat list of the values produced by mapfn
    """
    result = []
    for it in iterable:
        mret = mapfn(it)
        try:
            result.extend(mret)
        except TypeError:
            result.append(mret)
    return result


def flatten(iterable):
    """
    Flattens an iterable
    :param iterable: The iterable to be flattened
    :return: The flattened iterable as a list
    """
    return flatmap(iterable, identity)


def idistinct(iterable):
    """
    Function that returns an iterator over the distinct values in an iterable collection
    :param iterable: Some iterable collection
    :return: An iterator of the iterable's distinct values
    """
    return iter(set(iterable))


def distinct_by(iterable, keyfn):
    """
    Function that determines the distinct values of an iterable collection by
    applying a keyfn, that produces a unique key per item, to each item in the collection.
    Storing the unique key, item pairs.
    :param iterable: An iterable collection
    :param keyfn: Function that produces unique keys per each item in an iterable collection
    :return: An iterable of the collections distinct items
    """
    distinct = {}
    for item in iterable:
        key = keyfn(item)
        if key not in distinct:
            distinct[key] = item
    return distinct.values()


def distinct_by_fn(keyfn):
    """
    Creates a reusable distinct_by function that accepts an
    iterable collection and returns the collections distinct values.
    The distinct values are determined by applying a keyfn,
    that produces a unique key per item, to each item in the collection.
    Storing the unique key, item pairs.
    The reusable distinct_by function then returns an iterable of the unique items.
    :param keyfn: Function that produces unique keys per each item in an iterable collection
    :return: A reusable distinct_by function
    """
    def composed_distinct_by(iterable):
        distinct = {}
        for item in iterable:
            key = keyfn(item)
            if key not in distinct:
                distinct[key] = item
        return distinct.values()
    return composed_distinct_by


def group_by(iterable, keyfn):
    """
    Function that groups the values of an iterable collection using keyfun, a function
    that returns the key value for an item of the collection
    :param iterable: An iterable collection
    :param keyfn: Function that returns a unique key per each item
    :return: A dict of lists containing the values for each key produced by the keyfun
    """
    holder = defaultdict(list)
    for item in iterable:
        holder[keyfn(item)] = item
    return holder


def compose(*functions):
    """
    Function that composes all the function
    supplied as this functions argument together
    :param functions: Functions to compose
    :return: Single composed function
    """
    return reduce(lambda f, g: lambda x: f(g(x)), functions, identity)


def memoize(fn, cachesize=128, typed=False):
    """
    Memoizes the supplied function fn with the
    caveat that positional and keyword arguments are hashable.
    The memoization cache size is determined by the optional cachesize argument.
    Default cache size is 128.
    If the memoization function is to cache results for arguments based on the argument type,
    i.e 3 (int) vs 3.0 (float), supply type=True. Defaults to False.

    Implementation:
      @functools.lru_cache(maxsize=cachesize, typed=typed)
      def memowrapper(*args, **keywords):
          return fn(*args, **keywords)

    :param fn: The function to memoize
    :param cachesize: The size of the memoization cache. Defaults to 128.
    :param typed: Should the type of the argument be considered. Defaults to false.
    :return: The memoized function.
    """
    @lru_cache(maxsize=cachesize, typed=typed)
    def memowrapper(*args, **keywords):
        return fn(*args, **keywords)
    return memowrapper


def T(x=None):
    """
    Function that allways returns True
    :param x: Any value
    :return: True
    """
    return True


def F(x=None):
    """
    Function that always returns False
    :param x: Any value
    :return: False
    """
    return False
