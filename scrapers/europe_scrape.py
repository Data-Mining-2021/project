import pandas as pd
from main_scraper import scrape_tweets


handles = {'United Kingdom': ['BorisJohnson', '10DowningStreet', 'GOVUK', 'MayorofLondon'],
            'Italy': ['GiuseppeConteIT'],
            'Sweden': ['SwedishPM'],
            'Ukraine': ['Denys_Shmyhal']}

if __name__ == '__main__':
    tweetsDf = scrape_tweets(handles)

    # further convert to csv file format and export
    tweetsDf.to_csv('regions/Europe/europe_tweets.csv', index=False)