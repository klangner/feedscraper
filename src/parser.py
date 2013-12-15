# -*- coding: utf-8 -*-
'''
Created on 15-12-2013

@author: Krzysztof Langner
'''

import feedparser
import os.path
import datetime
import json

CONFIG_FOLDER = os.path.join(os.path.dirname(__file__), '../etc/')
OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), '../output/')


def getFeeds(url):
    items = []
    feed = feedparser.parse(url)
    for item in feed['items']:
        items.append({'link': item['link'],
                      'date': item['date'],
                      'title': item['title'],
                      'summary': item['summary']})
    return items
    
    
def parseFeeds(configFile):
    f = open(configFile, 'r')
    feeds = []
    for line in f.readlines():
        url = line.strip()
        if not url.startswith('#'):
            items = getFeeds(url)
            if len(items) == 0:
                print('No news for: ' + url)
            feeds.extend(items)
    return feeds
            
            
def saveFeeds(feeds, filepath):
    dateSuffix = datetime.datetime.now().strftime("%Y-%m-%dT%H")
    outputFilename = filepath + '-' + dateSuffix + '.json'
    f = open(outputFilename, 'w')
    json.dump(feeds, f)
    f.close()


if __name__ == '__main__':
    feeds = parseFeeds(CONFIG_FOLDER + 'gazetanews.txt')
    saveFeeds(feeds, OUTPUT_FOLDER + 'gazetanews')
    
    