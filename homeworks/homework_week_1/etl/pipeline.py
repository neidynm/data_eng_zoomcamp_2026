from .extract import donwload_green_trip_month, load_taxi_zone_lookup
from .config import logger, RAW_DIR, STAGING_DIR, TAXI_ZONE_TABLENAME
from .transform import clean_green_trip_data, save_transformed_data
from .load import load_to_db
from datetime import datetime
import pandas as pd
import os

def run_pipeline():
    try:
        logger.info(" Starting the ETL pipeline...")

        # Ensure directories exist
        RAW_DIR.mkdir(parents=True, exist_ok=True)
        STAGING_DIR.mkdir(parents=True, exist_ok=True)

        # Extract
        parquet_file = donwload_green_trip_month(month=11, year=2025)
        taxi_zone_file = load_taxi_zone_lookup()
        taxi_zone_data = pd.read_csv(os.path.join(STAGING_DIR,taxi_zone_file))

        if parquet_file:
            logger.info(f"Successfully downloaded: {parquet_file}")
        else:
            raise ValueError("Could not donwload file!")

        df_green_trip_data = pd.read_parquet(os.path.join(STAGING_DIR,parquet_file))

        df_green_trip_data_cleaned = clean_green_trip_data(df_green_trip_data)
        transformed_green_tx_data = save_transformed_data(df_green_trip_data_cleaned, parquet_file)


        if transformed_green_tx_data:
            logger.info(f"Successfully cleaned: {transformed_green_tx_data}")
        else:
            raise ValueError("Could not transform the data")
        load_to_db(df_green_trip_data_cleaned, 'green_trip')

        load_to_db(taxi_zone_data, TAXI_ZONE_TABLENAME)

    except ValueError as e:
        # Log the exception with the message and full traceback
        logger.exception(f"An error occured: {e}")
        # Re-raise the exception so it propagates upstream
        raise


if __name__ == "__main__":
    start = datetime.now()
    run_pipeline()
    duration = datetime.now() - start
    logger.info(f"⏱ Total time: {duration}")
