FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv dbt-duckdb duckdb

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy dependency files first (Docker caching)
COPY pyproject.toml uv.lock ./

# Install dependencies inside Docker
RUN uv sync

# Copy the rest of your project
COPY . .

WORKDIR /app/dbt

# Default command
CMD ["dbt", "run"]
