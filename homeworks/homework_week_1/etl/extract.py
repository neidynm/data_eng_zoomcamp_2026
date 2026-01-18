from .config import NYC_GREEN_FILENAME_TEMPLATE, NYC_GREEN_URL_TEMPLATE, logger, RAW_DIR, TAXI_ZONE_URL
from pathlib import Path
import requests
import os

def donwload_green_trip_month(month:int, year:int) ->list[Path]:
    url = NYC_GREEN_URL_TEMPLATE.format(year=year, month=month)
    filename = NYC_GREEN_FILENAME_TEMPLATE.format(year=year, month=month)

    filepath = os.path.join(RAW_DIR , filename)
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status() # Check if the download was successful (status code 200-299)
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): # Iterate in chunks
                    f.write(chunk)
        logger.info(f"Successfully downloaded: {filename}")
        return filepath
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to download {filename}: {e}")
        return None
    
def load_taxi_zone_lookup():
    filename = "taxi_zone.csv"

    filepath = os.path.join(RAW_DIR , filename)
    try:
        with requests.get(TAXI_ZONE_URL, stream=True) as r:
            r.raise_for_status() # Check if the download was successful (status code 200-299)
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): # Iterate in chunks
                    f.write(chunk)
        logger.info(f"Successfully downloaded: {filename}")
        return filepath
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to download {filename}: {e}")
        return None