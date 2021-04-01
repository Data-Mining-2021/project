import pandas as pd
from main_scraper import scrape_tweets


handles = {'South Africa': ['CyrilRamaphosa', 'DrZweliMkhize'], 
            'Liberia': ['GeorgeWeahOff'],
            'Nigeria': ['MBuhari', 'femigbaja']}

if __name__ == '__main__':
    tweetsDf = scrape_tweets(handles)

    # further convert to csv file format and export
    tweetsDf.to_csv('regions/Africa/africa_tweets.csv', index=False)

    # helpful for further tweaks later on
    # df = pd.read_csv('./Africa/African_tweets.csv')