
import re
import string
import numpy as np

from nltk.corpus import stopwords
from nltk.stem.isri import ISRIStemmer
from nltk.tokenize import TweetTokenizer

def process_tweet(tweet):
    
    stemmer = ISRIStemmer()
    stopwords_arabic = stopwords.words('arabic')
    # remove stock market tickers like $GE
    tweet = re.sub(r'\$\w*', '', tweet)
    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

    #remove english
    tweet = re.sub(r'[a-zA-Z]+', '', tweet)
    #removing the punctuation from the word
    punctuations = '@#!?+&*[]-%.:/();$=><|{}^' + "'`" + '_' + '...'
    for p in punctuations:
        tweet = tweet.replace(p,'') #Removing punctuatio
    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    tweets_clean = []
    for word in tweet_tokens:
        if word not in stopwords_arabic: 
            stem_word = stemmer.stem(word)  # stemming word
            tweets_clean.append(stem_word)

    return tweets_clean