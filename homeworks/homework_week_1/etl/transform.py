# etl/transform.py
from .config import logger, STAGING_DIR
import pandas as pd
from pathlib import Path

def clean_green_trip_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic cleaning on NYC Green Taxi trip data:
      - Convert datetimes
    """
    logger.info("🧹 Starting data cleaning...")

    # Example: Convert pickup and dropoff to datetime
    if 'lpep_pickup_datetime' in df.columns:
        df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'], errors='coerce')
    if 'lpep_dropoff_datetime' in df.columns:
        df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'], errors='coerce')

    logger.info(f"Data cleaned, remaining rows: {len(df)}")
    return df


def save_transformed_data(df: pd.DataFrame, filename: str) -> Path:
    """
    Save cleaned dataframe to processed directory as Parquet
    """
    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    output_path = STAGING_DIR / filename
    df.to_parquet(output_path, engine='pyarrow', index=False)
    logger.info(f" Transformed data saved to: {output_path}")
    return output_path
