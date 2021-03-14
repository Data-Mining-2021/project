import snscrape.modules.twitter as sntwitter
import pandas as pd


# note: removed 'WHO', since it was pulling random tweets
wordsToFilter = ['COVID', 'Kung-flu', 'Mask', 'Vaccine', 'Coronavirus', 'Sanitizer', 'Viral', 
    'Spread', 'Social distancing', '6 ft', 'Lockdown', 'Wuhan', 'Fauci', 'Pandemic' , 'CDC']

europeanTwitterHandles = {'United Kingdom': ['BorisJohnson', '10DowningStreet', 'GOVUK', 'MayorofLondon'],
                          'Italy': ['GiuseppeConteIT'],
                          'Sweden': ['SwedishPM'],
                          'Ukraine': ['Denys_Shmyhal']}

europeanTweets = []

if __name__ == '__main__':
    # concat strings to filter by
    textQuery = ' '.join([f'({phrase}) OR' for phrase in wordsToFilter])
    # remove extra 'OR'
    textQuery = textQuery[:len(textQuery) - 3]

    for country, twitterAccounts in europeanTwitterHandles.items():
        for account in twitterAccounts:
            # get all tweets from user that contain at least 1 of the query strings since 2020
            for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{textQuery} since:2020-01-01 from:{account}').get_items()):
                # if i > 100:
                #     break
                europeanTweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username, 
                    tweet.likeCount, tweet.replyCount, tweet.retweetCount, country])

    # convert to pandas data frame w/ column names
    tweetsDf = pd.DataFrame(europeanTweets, 
        columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Like Count', 'Reply Count', 'Retweet Count', 'Country'])

    # further convert to csv file format and export
    tweetsDf.to_csv('./europe/european_tweets.csv', index=False)