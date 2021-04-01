import pandas as pd
from main_scraper import scrape_tweets


handles = {'Israel': ['PresidentRuvi', 'IsraeliPM'], 
            'India': ['nsitharaman'],
            'South Korea': ['TheBlueHouseENG']}

if __name__ == '__main__':
    tweetsDf = scrape_tweets(handles)

    # further convert to csv file format and export
    tweetsDf.to_csv('regions/Asia/asia_tweets.csv', index=False)