all: force-data
data: $(DATA)

DATA=../regions/Europe/europe_tweets.csv ../regions/Africa/africa_tweets.csv ../regions/Pacific/pacific_tweets.csv \
../regions/South_America/south_america_tweets.csv ../regions/UN/un_tweets.csv \
../regions/North_America/north_america_tweets.csv ../regions/Asia/asia_tweets.csv

../regions/Europe/europe_tweets.csv: europe_scrape.py main_scraper.py
	py europe_scrape.py
../regions/Africa/africa_tweets.csv: africa_scrape.py main_scraper.py
	py africa_scrape.py
../regions/South_America/south_america_tweets.csv: south_america_scrape.py main_scraper.py
	py south_america_scrape.py
../regions/Pacific/pacific_tweets.csv: pacific_scrape.py main_scraper.py
	py pacific_scrape.py
../regions/UN/un_tweets.csv: un_scrape.py main_scraper.py
	py un_scrape.py
../regions/North_America/north_america_tweets.csv: north_america_scrape.py main_scraper.py
	py north_america_scrape.py
./regions/Asia/asia_tweets.csv: asia_scrape.py main_scraper.py
	py asia_scrape.py
force-data: 
	py un_scrape.py
	py pacific_scrape.py
	py south_america_scrape.py
	py africa_scrape.py
	py europe_scrape.py
	py north_america_scrape.py
	py asia_scrape.py