FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl build-essential

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app

# Copy everything into the container
COPY . .

# Install Python dependencies
RUN poetry config virtualenvs.create false && poetry install --no-root

# Set PYTHONPATH so FastAPI and Celery can find your app in src/
ENV PYTHONPATH=/app/src

# Default command: run FastAPI
CMD ["uvicorn", "myapp.main:app", "--host", "0.0.0.0", "--port", "8000"]
