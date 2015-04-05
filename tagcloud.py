import pickle
from operator import itemgetter
from collections import Counter

import matplotlib.pyplot as plt
from wordcloud import WordCloud

import sys
output = sys.argv[1]

kws = pickle.load(open('keywords.pkl', 'r'))

wc = WordCloud().generate(kws)

plt.imshow(wc)
plt.axis("off")
plt.savefig(output)
