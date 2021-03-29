all: data
data: $(DATA)

DATA=europe/european_tweets.csv africa/african_tweets.csv Pacific/pacific_tweets.csv \
South_America/south_america_tweets.csv UN/UN_tweets.csv

europe/european_tweets.csv: europe_scrape.py
	py europe_scrape.py
africa/african_tweets.csv: africa_scrape.py
	py africa_scrape.py
South_America/south_america_tweets.csv: south_america_scrape.py
	py south_america_scrape.py
Pacific/pacific_tweets.csv: pacific_scrape.py
	py pacific_scrape.py
UN/UN_tweets.csv: UN_scrape.py
	py UN_scrape.py