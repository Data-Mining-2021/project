all: data
data: $(DATA)

DATA=regions/Europe/europe_tweets.csv regions/Africa/africa_tweets.csv regions/Pacific/pacific_tweets.csv \
regions/South_America/south_america_tweets.csv regions/UN/un_tweets.csv

regions/Europe/europe_tweets.csv: scrapers/europe_scrape.py scrapers/main_scraper.py
	py scrapers/europe_scrape.py
regions/Africa/africa_tweets.csv: scrapers/africa_scrape.py scrapers/main_scraper.py
	py scrapers/africa_scrape.py
regions/South_America/south_america_tweets.csv: scrapers/south_america_scrape.py scrapers/main_scraper.py
	py scrapers/south_america_scrape.py
regions/Pacific/pacific_tweets.csv: scrapers/pacific_scrape.py scrapers/main_scraper.py
	py scrapers/pacific_scrape.py
regions/UN/un_tweets.csv: scrapers/un_scrape.py scrapers/main_scraper.py
	py scrapers/un_scrape.py