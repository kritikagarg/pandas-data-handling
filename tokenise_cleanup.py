import re
import operator
import nltk 
#from collections import Counter
#from nltk.corpus import stopwords
import string
#from nltk.stem import PorterStemmer

with open ("/mnt/analytics/TwitterData/KritikaData/Topics/data/stopwords.txt", 'r') as f:
        l1=f.read().splitlines()

punctuation = list(string.punctuation)
stop = l1 + punctuation + ['rt', 'via']

porter_stemmer = nltk.stem.PorterStemmer()
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

#lis=[]
with open ('ntweet', 'rt') as f:  
    for i,line in enumerate(f):
        words=[term for term in preprocess(line)]
        #stemmedwords =[porter_stemmer.stem(w) for w in words]
        #data_stem= words.apply(lambda words : [porter_stemmer.stem(w) for w in words])
	#print data_stem	
	cleanup = " ".join(filter(lambda word: word, words))
	print cleanup
	#lis.append(cleanup)

#f=open('tntweet','w')
#for i in range(len(lis)):
        #f.write(lis[i][0]+"\n")
#f.close()
