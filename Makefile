DATA=europe/european_tweets.csv
all: data
data: $(DATA)
europe/european_tweets.csv: europe_scrape.py
	py europe_scrape.py