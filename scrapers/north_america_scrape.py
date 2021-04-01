import pandas as pd
from main_scraper import scrape_tweets


handles = {'USA': ['joebiden', 'speakerpelosi', 'leadermcconnell', 'NYGovCuomo', 'GovRonDeSantis'], 
            'Canada': ['canada', 'JustinTrudeau', 'CanadianPM', 'fordnation']}

if __name__ == '__main__':
    tweetsDf = scrape_tweets(handles)

    # further convert to csv file format and export
    tweetsDf.to_csv('regions/North_America/north_america_tweets.csv', index=False)