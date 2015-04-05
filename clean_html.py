# -*- coding: utf-8 -*-
import codecs
import bleach
def clean(s):
    """
    >>> clean('<li>Data Warehouse platforms or massively parallel processing databases </li></ul>- Online advertising analytic platforms using any of the following: <ul><li>Machine learning, e.g., feature discovery, formula optimization, text classification </li><li>Natural language processing, e.g., linguistics, text analysis, information retrieval </li><li>Statistical modeling techniques, e.g., logistic regression, decision trees, SVMs, neural networks </li></ul>- Search engines and web-based information extraction techniques  - Data mining, optimization, analysis of very large data sets')
    u'Data Warehouse platforms or massively parallel processing databases - Online advertising analytic platforms using any of the following: Machine learning, e.g., feature discovery, formula optimization, text classification Natural language processing, e.g., linguistics, text analysis, information retrieval Statistical modeling techniques, e.g., logistic regression, decision trees, SVMs, neural networks - Search engines and web-based information extraction techniques  - Data mining, optimization, analysis of very large data sets'
    """
    return bleach.clean(s.replace(u"–", u"-"), strip = True, tags = [])

if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    output = sys.argv[2]
    
    with codecs.open(path, 'r', 'utf8') as f:
        with codecs.open(output, 'w' 'utf8') as o:
            for l in f:
                cleaned_l = clean(l)
                o.write(cleaned_l.encode('utf8'))
    
