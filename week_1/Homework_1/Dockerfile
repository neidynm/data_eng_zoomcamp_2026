FROM python:3.13-slim

WORKDIR /app

# Install uv tool (if using pdm/uv)
RUN pip install uv

# Copy dependency files first for caching
COPY pyproject.toml uv.lock* ./

# Install dependencies
RUN uv sync

# Copy the project code
COPY . .

# Default command: run as a module so relative imports work
CMD ["uv", "run", "-m", "etl.pipeline"]
