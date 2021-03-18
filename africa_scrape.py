import snscrape.modules.twitter as sntwitter
import pandas as pd
import re

# Single-line regex for urls:
reg = "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"


# note: removed 'WHO', since it was pulling random tweets
wordsToFilter = ['COVID', 'Kung-flu', 'Mask', 'Vaccine', 'Coronavirus', 'Sanitizer', 'Viral', 
    'Spread', 'Social distancing', '6 ft', 'Lockdown', 'Wuhan', 'Fauci', 'Pandemic' , 'CDC']

africanTwitterHandles = {'South Africa': ['CyrilRamaphosa', 'DrZweliMkhize'], 
                         'Liberia': ['GeorgeWeahOff'],
                         'Nigeria': ['MBuhari', 'femigbaja']}

africanTweets = []

if __name__ == '__main__':
    # concat strings to filter by
    # textQuery = ' '.join([f'({phrase}) OR' for phrase in wordsToFilter])
    # # remove extra 'OR'
    # textQuery = textQuery[:len(textQuery) - 3]

    # for country, twitterAccounts in africanTwitterHandles.items():
    #     for account in twitterAccounts:
    #         # get all tweets from user that contain at least 1 of the query strings since 2020
    #         for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{textQuery} since:2020-01-01 from:{account}').get_items()):
    #             # if i > 100:
    #             #     break
    #             africanTweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username, 
    #                 tweet.likeCount, tweet.replyCount, tweet.retweetCount, country])

    # # convert to pandas data frame w/ column names
    # tweetsDf = pd.DataFrame(africanTweets, 
    #     columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Like Count', 'Reply Count', 'Retweet Count', 'Country'])

    # # further convert to csv file format and export
    # tweetsDf.to_csv('./africa/african_tweets.csv', index=False)

    df = pd.read_csv('./africa/african_tweets.csv')

    for index in df.index:
        df.loc[index, 'Text'] = re.sub(reg, '', df.loc[index, 'Text'])

    df.to_csv('./africa/african_tweets_new.csv', index=False)