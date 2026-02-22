/* @bruin
name: reports.trips_report

# TODO: Set platform type.
# Docs: https://getbruin.com/docs/bruin/assets/sql
# suggested type: duckdb.sql
type: duckdb.sql

# TODO: Declare dependency on the staging asset(s) this report reads from.
depends:
  - staging.trips

# TODO: Choose materialization strategy.
# For reports, `time_interval` is a good choice to rebuild only the relevant time window.
# Important: Use the same `incremental_key` as staging (e.g., pickup_datetime) for consistency.
materialization:
  type: table
  strategy: time_interval
  incremental_key: pickup_datetime
  time_granularity: timestamp

# TODO: Define report columns + primary key(s) at your chosen level of aggregation.
columns:
  - name: pickup_datetime
    type: timestamp
    primary_key: true
    checks:
      - name: not_null

@bruin */

-- Purpose of reports:
-- - Aggregate staging data for dashboards and analytics
-- Required Bruin concepts:
-- - Filter using `{{ start_datetime }}` / `{{ end_datetime }}` for incremental runs
-- - GROUP BY your dimension + date columns

SELECT * -- TODO: replace with your aggregation logic
FROM staging.trips
WHERE pickup_datetime >= '{{ start_datetime }}'
  AND pickup_datetime < '{{ end_datetime }}'
