import sys, fileinput, itertools
from collections import defaultdict
import nltk
import spacy

nlp = spacy.load('en')

ngram_sentence = defaultdict(list)
high_freq_words = set([line.strip() for line in fileinput.input('high_freq_words.txt')])
prons = set([line.strip() for line in fileinput.input('prons.txt')])
collocation = set([(tk[0], tk[2]) for line in fileinput.input('collocation.txt') for tk in [line.strip().split('\t')]])

def lemmatize_sent(sentence):
    return [tk.lemma_ for tk in nlp(sentence)]

def calculate_score(ngram, sentence):
    ##### YOUR CODE HERE #####
    ngram = lemmatize_sent(ngram)
    sentence = list(filter(('\xa0 ').__ne__, lemmatize_sent(sentence)))
    sent_perm = itertools.permutations(sentence, 2)
    
    try:
        locat = list(zip(*[sentence[i:] for i in range(len(ngram))])).index(tuple(ngram))
    except:
        return -999
        
    not_in_high_freq = len([word for word in sentence if word not in high_freq_words])
    is_prons = len([word for word in sentence if word in prons])
    is_collocation = len(list(set([words for words in sent_perm if words in collocation])))
    
    score = locat - not_in_high_freq - is_prons + is_collocation

    return score


for line in fileinput.input():
    ngram, sentence = line.strip().split('\t')
    ngram_sentence[ngram].append(sentence)

for ngram, sentences in ngram_sentence.items():
    best_sentence = sorted(sentences, key=lambda s: calculate_score(ngram, s), reverse=True)[:3]
    print(ngram + '\t' + '\t'.join(best_sentence))
