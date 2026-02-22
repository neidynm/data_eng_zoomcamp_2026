"""@bruin

name: ingestion.trips
connection: duckdb-default

materialization:
  type: table
  strategy: append
image: python:3.11

@bruin"""

import os
import json
import requests
import pandas as pd
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from io import BytesIO


def materialize():
    """
    Ingests NY taxi trip data using Bruin runtime context.
    Fetches Parquet files from the TLC public dataset for each taxi type
    and each month within the BRUIN date window.
    """

    # ── 1. Bruin runtime variables ────────────────────────────────────────────

    start_date = datetime.strptime(os.environ["BRUIN_START_DATE"], "%Y-%m-%d")
    end_date   = datetime.strptime(os.environ["BRUIN_END_DATE"],   "%Y-%m-%d")

    # Pipeline variables – BRUIN_VARS is a JSON string
    bruin_vars  = json.loads(os.environ.get("BRUIN_VARS", "{}"))
    taxi_types  = bruin_vars.get("taxi_types", ["yellow", "green", "fhv"])

    # ── 2. Generate (taxi_type, year, month) combos for the window ────────────

    BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"

    def iter_months(start: datetime, end: datetime):
        cur = start.replace(day=1)
        while cur <= end:
            yield cur.year, cur.month
            cur += relativedelta(months=1)

    endpoints = [
        {
            "taxi_type": taxi_type,
            "year": year,
            "month": month,
            "url": f"{BASE_URL}/{taxi_type}_tripdata_{year}-{month:02d}.parquet",
        }
        for taxi_type in taxi_types
        for year, month in iter_months(start_date, end_date)
    ]

    # ── 3. Fetch, parse, tag ──────────────────────────────────────────────────

    extracted_at = datetime.now(timezone.utc)
    frames = []

    for ep in endpoints:
        print(f"Fetching {ep['url']} ...")
        try:
            response = requests.get(ep["url"], timeout=120)
            response.raise_for_status()
        except requests.HTTPError as exc:
            # Some month/type combos don't exist yet – skip gracefully
            print(f"  Skipped ({exc.response.status_code}): {ep['url']}")
            continue

        df = pd.read_parquet(BytesIO(response.content))

        # Lineage / debugging columns
        df["taxi_type"]    = ep["taxi_type"]
        df["source_year"]  = ep["year"]
        df["source_month"] = ep["month"]
        df["extracted_at"] = extracted_at   # single timestamp for the whole run

        frames.append(df)

    if not frames:
        raise RuntimeError(
            f"No data fetched for window {start_date.date()} → {end_date.date()} "
            f"and taxi_types={taxi_types}. Check the date range or taxi_type names."
        )

    # ── 4. Concatenate and return ─────────────────────────────────────────────
    # Bruin writes whatever is returned by materialize() to the destination.
    # Columns that differ across taxi types are fine – Bruin handles schema evolution.

    final_df = pd.concat(frames, ignore_index=True)
    print(f"Total rows ingested: {len(final_df):,}")
    return final_df
