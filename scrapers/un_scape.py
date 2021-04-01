import pandas as pd
from main_scraper import scrape_tweets


handles = {'UN': ['antonioguterres', 'AminaJMohammed', 'volkan_bozkir']}

if __name__ == '__main__':
    tweetsDf = scrape_tweets(handles)

    # further convert to csv file format and export
    tweetsDf.to_csv('regions/UN/un_tweets.csv', index=False)