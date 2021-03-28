DATA=europe/european_tweets.csv
all: data
data: $(DATA)
europe/european_tweets.csv: europe_scrape.py
	python europe_scrape.py