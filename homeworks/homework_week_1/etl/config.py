import os
from pathlib import Path
import logging

# -------------------------
# ENVIRONMENT VARIABLES
# -------------------------
POSTGRES_USER = os.getenv("POSTGRES_USER", "nyc")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "changeme")
POSTGRES_DB = os.getenv("POSTGRES_DB", "yellow_taxi")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))

# NYC Taxi dataset URL template (can be extended by month)
NYC_GREEN_URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year}-{month:02d}.parquet"
NYC_GREEN_FILENAME_TEMPLATE = "green_tripdata_{year}-{month:02d}.parquet"
TAXI_ZONE_URL = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
TAXI_ZONE_TABLENAME = "taxi_zone_lookup"

# -------------------------
# PATHS
# -------------------------
BASE_DIR = Path(__file__).parent.parent.resolve()
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
STAGING_DIR = DATA_DIR / "staging"
LOG_DIR = BASE_DIR / "logs"

# Ensure directories exist
for path in [RAW_DIR, STAGING_DIR, LOG_DIR]:
    path.mkdir(parents=True, exist_ok=True)

# -------------------------
# DATABASE CONNECTION STRING
# -------------------------
DB_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
DB_URI_LOCAL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:{POSTGRES_PORT}/{POSTGRES_DB}"

# -------------------------
# LOGGING CONFIGURATION
# -------------------------
LOG_FILE = LOG_DIR / "etl_pipeline.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
