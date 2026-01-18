# Data Engineering Zoomcamp 2026 - Week 1 Homework Assignment


## Overview

This repository contains the solution for Week 1 homework of the Data Engineering Zoomcamp 2026. The assignment focuses on building a complete ETL (Extract, Transform, Load) pipeline using Docker, PostgreSQL, and Python to process NYC Green Taxi trip data from November 2025.

## Project Structure

```
homework_week_1/
├── etl/
│   ├── __init__.py           # Package initialization and exports
│   ├── config.py             # Configuration settings and environment variables
│   ├── extract.py            # Data extraction functions
│   ├── transform.py          # Data transformation and cleaning
│   ├── load.py               # Database loading functions
│   └── pipeline.py           # Main ETL pipeline orchestration
├── data/
│   ├── raw/                  # Downloaded raw data files
│   └── staging/              # Transformed data ready for loading
├── logs/                     # ETL pipeline execution logs
├── Analysis_green_taxi_data.ipynb    # Jupyter notebook with homework queries
├── Dockerfile                # Docker image configuration
├── docker-compose.yml        # Multi-container orchestration
├── makefile                  # File with commands to run the pipeline
├── pyproject.toml            # Project dependencies
└── README.md                 # This file
```

## Prerequisites

Before running this project, ensure you have the following installed:

- Docker (version 20.10 or higher)
- Docker Compose (version 2.0 or higher)
- Python 3.13 or higher
- pip (Python package manager)

## Technologies Used

This project leverages the following technologies:

- **Docker**: Containerization platform ensuring consistent development environments across different systems
- **Docker Compose**: Tool for defining and running multi-container applications with a single configuration file
- **PostgreSQL**: Relational database management system for storing and querying taxi trip data
- **pgAdmin**: Web-based database administration tool for managing PostgreSQL databases
- **Python 3.13**: Core programming language for the ETL pipeline
- **pandas**: Powerful data manipulation and analysis library
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping library for database interactions
- **pyarrow**: Library for reading Parquet files efficiently
- **requests**: HTTP library for downloading datasets from remote sources
- **Jupyter Notebook**: Interactive computing environment for data analysis and visualization

## Dataset Information

The project processes two primary datasets from the NYC Taxi and Limousine Commission:

**Green Taxi Trip Data (November 2025)**: Contains detailed information about green taxi trips including pickup and dropoff timestamps, locations, distances, fare amounts, payment types, and passenger counts. The data is sourced from the official NYC TLC trip record data repository in Parquet format.

**Taxi Zone Lookup Table**: Provides the mapping between location IDs and actual zone names, boroughs, and service zones across New York City. This reference table enables geographic analysis of the trip data.

## Environment Configuration

The ETL pipeline uses environment variables for database configuration, with sensible defaults provided:

```
POSTGRES_USER=nyc
POSTGRES_PASSWORD=changeme
POSTGRES_DB=yellow_taxi
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

These variables can be customized by creating a `.env` file in the project root directory or by modifying the values in `docker-compose.yml`.

## Installation and Setup

### Step 1: Clone the Repository

Begin by cloning the repository and navigating to the homework directory:

```bash
git clone https://github.com/neidynm/data_eng_zoomcamp_2026.git
cd data_eng_zoomcamp_2026/homeworks/homework_week_1
```

### Step 2: Install Python Dependencies

Install the required Python packages for running the ETL pipeline and analysis notebook:

```bash
pip install pandas sqlalchemy psycopg2-binary pyarrow requests python-dotenv jupyter
```

### Step 3: Start Docker Services

Launch the PostgreSQL database and pgAdmin containers using Docker Compose:

```bash
docker-compose up -d
```

This command starts the following services in detached mode:
- PostgreSQL database server on port 5432
- pgAdmin web interface on port 8080

### Step 4: Access Database Tools

Once the containers are running, you can access pgAdmin by navigating to `http://localhost:8080` in your web browser. Use the credentials specified in your `docker-compose.yml` file to log in and configure the connection to the PostgreSQL database.

## ETL Pipeline Architecture

The ETL pipeline is organized into modular components following software engineering best practices:

### Extract Phase

The extraction module (`extract.py`) handles downloading data from remote sources. It implements two primary functions:

`donwload_green_trip_month(month, year)` downloads the NYC Green Taxi trip data for a specified month and year from the official CloudFront distribution. The function uses streaming downloads to efficiently handle large files and includes comprehensive error handling.

`load_taxi_zone_lookup()` retrieves the taxi zone reference data that maps location IDs to human-readable zone names and borough information.

Both functions save downloaded files to the `data/raw` directory and log their progress for monitoring and debugging purposes.

### Transform Phase

The transformation module (`transform.py`) performs data cleaning and preparation operations:

`clean_green_trip_data(df)` processes the raw taxi trip data by converting pickup and dropoff timestamps to proper datetime objects, handling any conversion errors gracefully. The function returns a cleaned DataFrame ready for analysis and database loading.

`save_transformed_data(df, filename)` persists the cleaned data to the staging directory in Parquet format, maintaining efficient storage and fast loading characteristics.

### Load Phase

The loading module (`load.py`) handles database operations through SQLAlchemy:

`load_to_db(df, table_name)` takes a pandas DataFrame and
