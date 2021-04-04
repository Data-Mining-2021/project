import pandas as pd
from main_scraper import scrape_tweets


handles = {'Chile': ['mbachelet']}

if __name__ == '__main__':
    tweetsDf = scrape_tweets(handles)

    # further convert to csv file format and export
    tweetsDf.to_csv('../regions/South_America/south_america_tweets.csv', index=False)
