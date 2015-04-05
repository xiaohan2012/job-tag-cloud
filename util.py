import pickle
import codecs

def read_keywords(path):
    keywords = []
    with codecs.open(path, 'r', 'utf8') as f:
        for l in f:
            keywords += l.split('\t')

    return keywords

def dump_keywords(obj, path):
    pickle.dump(obj, open(path, 'w'))

def load_keywords(obj, path):
    return pickle.load(open(path, 'r'))

if __name__ == "__main__":
    kws = read_keywords('job_keywords.txt')
    dump_keywords(kws, 'keywords.pkl')
