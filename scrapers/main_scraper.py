import snscrape.modules.twitter as sntwitter
import pandas as pd
import re

# regex for urls
reg = "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"

tweets = []

def scrape_tweets(handles):
    for country, twitterAccounts in handles.items():
        for account in twitterAccounts:
            for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'since:2020-01-01 from:{account}').get_items()):
                tweets.append([tweet.date, tweet.id, tweet.content, tweet.user.username, 
                    tweet.likeCount, tweet.replyCount, country])

    # convert to pandas data frame w/ column names
    tweetsDf = pd.DataFrame(tweets, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Like Count', 'Reply Count', 'Country'])

    # filter out urls
    for index in tweetsDf.index:
        tweetsDf.loc[index, 'Text'] = re.sub(reg, '', tweetsDf.loc[index, 'Text'])

    return tweetsDf