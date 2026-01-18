# Make key objects available at package level for convenience
from .config import logger, DB_URI, RAW_DIR, STAGING_DIR, NYC_GREEN_FILENAME_TEMPLATE, TAXI_ZONE_TABLENAME, DB_URI_LOCAL

__all__ = ["logger", "DB_URI","DB_URI_LOCAL","TAXI_ZONE_URL", "TAXI_ZONE_TABLENAME", "RAW_DIR", "STAGING_DIR", "NYC_GREEN_FILENAME_TEMPLATE"]