rootdir = $(realpath .)

all: force-data
data: $(DATA)

DATA=$(rootdir)/regions/Europe/europe_tweets.csv $(rootdir)/regions/Africa/africa_tweets.csv $(rootdir)/regions/Pacific/pacific_tweets.csv \
$(rootdir)/regions/South_America/south_america_tweets.csv $(rootdir)/regions/UN/un_tweets.csv

$(rootdir)/regions/Europe/europe_tweets.csv: $(rootdir)/scrapers/europe_scrape.py $(rootdir)/scrapers/main_scraper.py
	py $(rootdir)/scrapers/europe_scrape.py
$(rootdir)/regions/Africa/africa_tweets.csv: $(rootdir)/scrapers/africa_scrape.py $(rootdir)/scrapers/main_scraper.py
	py $(rootdir)/scrapers/africa_scrape.py
$(rootdir)/regions/South_America/south_america_tweets.csv: $(rootdir)/scrapers/south_america_scrape.py $(rootdir)/scrapers/main_scraper.py
	py $(rootdir)/scrapers/south_america_scrape.py
$(rootdir)/regions/Pacific/pacific_tweets.csv: $(rootdir)/scrapers/pacific_scrape.py $(rootdir)/scrapers/main_scraper.py
	py $(rootdir)/scrapers/pacific_scrape.py
$(rootdir)/regions/UN/un_tweets.csv: $(rootdir)/scrapers/un_scrape.py $(rootdir)/scrapers/main_scraper.py
	py $(rootdir)/scrapers/un_scrape.py
force-data: 
	py $(rootdir)/scrapers/un_scrape.py
	py $(rootdir)/scrapers/pacific_scrape.py
	py $(rootdir)/scrapers/south_america_scrape.py
	py $(rootdir)/scrapers/africa_scrape.py
	py $(rootdir)/scrapers/europe_scrape.py