# Use slim base image
FROM python:3.10-slim

ENV POETRY_VERSION=1.7.1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


# Install Poetry
# Install Poetry and build tools
RUN apt-get update \
    && apt-get install --no-install-recommends -y curl build-essential gcc \
    && pip install "poetry==$POETRY_VERSION" \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy only dependency files first for caching
COPY pyproject.toml poetry.lock* /app/

# Disable Poetry virtualenv creation (we're already in a container)
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Now copy the rest of the app
COPY . /app

RUN python --version

# Run tests by default (can be overridden)
CMD ["poetry", "run", "pytest"]
