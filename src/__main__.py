import credentials
import src.data_scraper.time_helpers
from src import config
from src.data_scraper import data_scraper, time_helpers
from src import utils
import time


if __name__ == '__main__':

    # TESTING NEW STRUCTURE
    # Initializing the timestamps to use in all data scrapers
    end_timestamp = time_helpers.get_current_timestamp()
    training_start_timestamp = time_helpers.get_training_start_timestamp(end_timestamp=end_timestamp)
    production_start_timestamp = time_helpers.get_production_start_timestamp(end_timestamp=end_timestamp)


    # Exchange data
    BinanceScraper = data_scraper.Binance()

    # binance_historical_df = BinanceScraper.get_data(
    #     start_time=training_start_timestamp, end_time=end_timestamp, overwrite=False)
    # print(binance_historical_df.head())

    binance_latest_df = BinanceScraper.get_data(
        start_time=production_start_timestamp, end_time=end_timestamp, overwrite=True)
    print(binance_latest_df.head())


    # Twitter Generic Tweets
    TwitterGenericScraper = data_scraper.TwitterGeneric()

    # historical_generic_tweets = TwitterGenericScraper.get_data(
    #     start_timestamp=training_start_timestamp, end_timestamp=end_timestamp, save_checkpoint=False, overwrite=True)
    # print(historical_generic_tweets.tail())

    latest_generic_tweets = TwitterGenericScraper.get_data(
        start_timestamp=production_start_timestamp, end_timestamp=end_timestamp, save_checkpoint=False, overwrite=True)
    print(latest_generic_tweets.tail())


    # Twitter Profiles with timestamp
    TwitterProfilesScraper = data_scraper.TwitterProfiles()

    # historical_profile_tweets = TwitterProfilesScraper.get_data(
    #     start_timestamp=training_start_timestamp, end_timestamp=end_timestamp, save_checkpoint=False, overwrite=True)
    # print(historical_profile_tweets.tail())

    latest_profile_tweets = TwitterProfilesScraper.get_data(
        start_timestamp=production_start_timestamp, end_timestamp=end_timestamp, save_checkpoint=False, overwrite=True)
    print(latest_profile_tweets.tail())










