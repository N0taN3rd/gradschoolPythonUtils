def import_clazz(name):
    """
    Dynamically import a class from a module.
    From https://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class
    :param name: Class specifier in the form of 'a.b.c.class'
    :return: Imported class
    """
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def get_tokenizer(tokenizer):
    if isinstance(tokenizer, str):
        return import_clazz('nltk.tokenize.%s' % tokenizer)
    elif callable(tokenizer):
        return tokenizer()
    else:
        return tokenizer
