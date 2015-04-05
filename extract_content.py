from lxml import etree
parser = etree.XMLParser(ns_clean=True)

def extract(path, field, multiple=True):
    """
    >>> extract('jobs/11335995.json', 'description', False) # doctest: +ELLIPSIS
    Like Google's own ambitions...
    >>> extract('data/0.json', 'description-snippet', True) # doctest: +ELLIPSIS
    IBM Research...
    """
    tree = etree.parse(path, parser)
    if multiple:
        path = 'jobs/job/%s' %(field)
    else:
        path = '/job/%s' %(field)
    for snippet in tree.xpath(path):
        print unicode(snippet.text).encode('utf8')


if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    field = sys.argv[2]
    multiple = int(sys.argv[3])

    extract(path, field, multiple)
