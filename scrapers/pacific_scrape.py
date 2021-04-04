import pandas as pd
from main_scraper import scrape_tweets


handles = {'Australia': ['ScottMorrisonMP', 'GregHuntMP'],
            'New Zealand': ['jacindaardern', 'AndrewLittleMP']}

if __name__ == '__main__':
    tweetsDf = scrape_tweets(handles)

    # further convert to csv file format and export
    tweetsDf.to_csv('../regions/Pacific/pacific_tweets.csv', index=False)