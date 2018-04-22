
def href_not_hash(tag):
    """
    BeautifulSoup filter function that returns
    false if the tag is None, does not have the href attribute
    or the href attribute of the tag starts with #
    :param tag: The tag to check
    :return: Returns true if the href attribute does not start with #
    """
    if tag is None:
        return False
    elif tag.has_attr('href'):
        return tag['href'][0] != '#'
    else:
        return False


__tags_url_attr = dict(
    applet=['codebase', 'archive'],
    body='background',
    blockquote='cite',
    button='formaction',
    command='icon',
    form='action',
    image='xlink:href',
    meta='content',
    param='value',
    object=['codebase', 'data'],
    q='cite',
    video='poster'
)
__tags_url_attr['del'] = 'cite'


def url_attrs(tag):
    """
    BeautifulSoup filter function that returns
    false if the tag is None, or does not have a known attribute that may contain a URL
    :param tag: The tag to check
    :return: True if the tag contains an attribute that may contain a URL
    """
    if tag is None:
        return False
    if tag.has_attr('href') or tag.has_attr('src') or tag.has_attr('srcset'):
        return True
    check = __tags_url_attr.get(tag.name, None)
    if check is not None:
        if isinstance(check, list):
            for attr in check:
                if tag.has_attr(attr):
                    return True
        else:
            return tag.has_attr(check)
    return False
