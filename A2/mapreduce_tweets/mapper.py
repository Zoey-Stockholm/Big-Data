#!/usr/bin/env python3
"""mapper.py"""
import json
import re
import sys
han ='han'
hon = 'hon'
den = 'den'
det = 'det'
denna = 'denna'
denne = 'denne'
hen ='hen'
uni_tweets = 'uni_tweets'


for line in sys.stdin:
    # handle the fact that some are empty line
    if line!='\n':
        tweet = json.loads(line)

        # check if it is a retweet
        if 'retweeted_status' in tweet: # a retweet
            print('retweet',1)
            #continue
        else:                           # unique tweet
            print(uni_tweets,1)
            # use re.search to check if the case-insensitive pattern given exists in the tweet
            if re.search(han,tweet['text'],re.IGNORECASE):
                print(han,1)
            if re.search(hon,tweet['text'],re.IGNORECASE):
                print(hon,1)
            if re.search(den,tweet['text'],re.IGNORECASE):
                print(den,1)
            if re.search(det,tweet['text'],re.IGNORECASE):
                print(det,1)
            if re.search(denna,tweet['text'],re.IGNORECASE):
                print(denna,1)
            if re.search(denne,tweet['text'],re.IGNORECASE):
                print(denne,1)
            if re.search(hen,tweet['text'],re.IGNORECASE):
                print(hen,1)
                