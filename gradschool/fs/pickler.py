import pickle


def dump_pickle(obj, file):
    """
    Serialize a python object/class using pickle
    :param obj: The python object/class to pickle
    :param file: Path to file to be saved
    """
    with open(file, 'wb') as out:
        pickle.dump(obj, out)


def read_pickle(name):
    """
    Reads a pickle file
    :param name: Path to the pickled file to read
    :return: The deserialized pickled file
    """
    with open(name, "rb") as input_file:
        return pickle.load(input_file)
