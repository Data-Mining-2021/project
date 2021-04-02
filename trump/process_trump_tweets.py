import pandas as pd
import re


# regex for urls
reg = "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"

# original format:
#   id,text,isRetweet,isDeleted,device,favorites,retweets,date,isFlagged
# updated format:
#   Datetime,Tweet Id,Text,Username,Like Count,Retweet Count,Country

# NOTE: not including 'Username' and 'Country' for now - will modify later if necessary

# load data
df = pd.read_csv('trump/trump_tweets_raw.csv')

# drop useless columns
df = df.drop(columns=['isDeleted', 'device', 'isFlagged'])

# remove retweets
df = df[df['isRetweet'] == 'f']

# now remove that identifier
df = df.drop(columns=['isRetweet'])

# rename columns to match convention
df = df.rename(columns={'id': 'Tweet Id', 'text': 'Text', 'favorites': 'Like Count', 
                    'retweets': 'Retweet Count', 'date': 'Datetime'})

# rearrange columns to match convention
df = df[['Datetime', 'Tweet Id', 'Text', 'Like Count', 'Retweet Count']]

# filter out urls
for index in df.index:
    df.loc[index, 'Text'] = re.sub(reg, '', df.loc[index, 'Text'])

# export to a new csv
df.to_csv('trump/trump_tweets.csv', index=False)

