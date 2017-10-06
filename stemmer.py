import sys
import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import *


def tokenize(tweets):
    tokenizer = nltk.TweetTokenizer()
    cleaned = clean_text(tweets)
    tweets_tokenized = (tokenizer.tokenize(cleaned))
    return tweets_tokenized

def clean_text(text):
    strip_urls = re.sub(r"http\S+", "", text)
    #print strip_urls
    strip_punctuation = ''.join(char for char in strip_urls if char not in string.punctuation)
    #print strip_punctuation
    clean_text = strip_punctuation.lower()
    #print clean_text
    return clean_text


def remove_stopwords(tweet):
    stop = set(stopwords.words('english'))
    # add some tweet-specific terms for stopword list
    stop.update(('rt', ':', ',', '.'))
    tweets_stop = [token for token in tweet if token not in stop]
    return tweets_stop

def stem(tweet):
    stemmer = PorterStemmer()
    stemmed_tweets = []
    # do not stem user mentions
    stemmed_tweets = [stemmer.stem(token) if token[0] != '@' else token for token in tweet]
    return stemmed_tweets

tweets= []
with open ('nfhtweet.txt', 'rt') as f, open('cleantweet.txt','w') as f1 :
# open file of tweets to parse
    for line in f:
    	tokenized = tokenize(line)
    	stop_removed = remove_stopwords(tokenized)
        stemmed = stem(stop_removed)
        stemmed = [x.encode('ascii','ignore') for x in stemmed]
        #print stemmed
        line = " ".join(stemmed)
        f1.write("{}\n".format(line))




