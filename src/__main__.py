import credentials
import src.data_scraper.scraper_binance
import src.data_scraper.time_helpers
from src import config
from src.data_scraper import scraper_twitter, time_helpers
from src import utils
import time


if __name__ == '__main__':
    # Initializing the timestamps to use in all data scrapers
    end_timestamp = time_helpers.get_current_timestamp()
    training_start_timestamp = time_helpers.get_training_start_timestamp(end_timestamp=end_timestamp)
    production_start_timestamp = time_helpers.get_production_start_timestamp(end_timestamp=end_timestamp)

    # Exchange data
    # Dev mode
    BinanceScraper = src.data_scraper.scraper_binance.BinanceScraper(dev_run=True)
    training_data = BinanceScraper.get_data(training_start_timestamp, end_timestamp)
    print(training_data.tail())

    # Prod mode
    BinanceScraper = src.data_scraper.scraper_binance.BinanceScraper(dev_run=False)
    prod_data = BinanceScraper.get_data(production_start_timestamp, end_timestamp)
    print(prod_data.tail())










