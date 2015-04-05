from alchemyapi import AlchemyAPI
import json
import codecs 

alchemyapi = AlchemyAPI()

def extract(text):
    response = alchemyapi.keywords('text', text, {'sentiment': 1})
    if response['status'] == 'OK':
        return [r['text'] for r in response['keywords']]
    else:
        raise Exception('Error in keyword extaction call: ', response['statusInfo'])

if __name__ == "__main__":
    import sys
    path = sys.argv[1]

    with codecs.open(path, 'r', 'utf8') as f:
        for i,l in enumerate(f):
            if i%10 == 0:
                sys.stderr.write('%d finished\n' %i)
            kws = extract(l)
            print '\t'.join(kws).encode('utf8')

