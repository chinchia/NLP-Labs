import sys, fileinput
import re
import nltk

def tokens(s): return(nltk.word_tokenize(s))

def is_ngram(ngram):
    if ngram.lower() in ngram_set:
        return True

ngram_set = set([line.strip() for line in fileinput.input('nc.txt')])
#ngram_set = [tuple(x.split(' ')) for x in ngram_set]

for line in fileinput.input():
    sent = tokens(line)
    ##### YOUR CODE HERE #####
    if len(sent) >= 10 and len(sent) <= 25:
        for n in range(2, 6):
            words = zip(*[sent[i:] for i in range(n)])
            for i in list(words):
                #i = tuple([x.lower() for x in i])
                word = ' '.join(i)
                if is_ngram(word):
                    sys.stdout.write(('{}\t{}'.format(word, line)))
                    