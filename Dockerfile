# Stage 1: Builder
FROM python:3.11-slim-bullseye AS builder

WORKDIR /app

# Install system dependencies needed for building Python packages (e.g., psycopg2-binary)
# curl and netcat are useful for health checks and debugging.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    netcat && \
    rm -rf /var/lib/apt/lists/*

# Create virtual environment
# This helps isolate dependencies and is more efficient for Docker caching.
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy the requirements.txt and install dependencies
# This step is placed early to leverage Docker's build cache.
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
# Use a slim base image for the final runtime image to keep it small.
FROM python:3.11-slim-bullseye

WORKDIR /app

# Install only runtime dependencies
# libpq5 is needed for PostgreSQL connectivity.
# curl and netcat are still useful for health checks and debugging in the final image.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    netcat && \
    rm -rf /var/lib/apt/lists/*

# Copy virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Create a non-root user for security best practices
RUN useradd -m appuser && \
    mkdir -p /app/static /app/media && \
    chown -R appuser:appuser /app
USER appuser

# Copy application code
COPY --chown=appuser:appuser . .

# Fix line endings and permissions for the entrypoint script
RUN sed -i 's/\r$//' docker-entrypoint.sh && \
    chmod +x docker-entrypoint.sh

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=myproject.settings

# Declare the ports the container will listen on.
# These are informational but good practice. GCP will primarily look at the PORT env var.
EXPOSE 8000
EXPOSE 8080

# Health check configuration
# Uses the PORT environment variable to check the dynamically bound port.
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT:-8080}/health/ || exit 1 # Use PORT, fallback to 8080

# Entrypoint script that will run before the main command
ENTRYPOINT ["./docker-entrypoint.sh"]

# Default command to run the Gunicorn server
# Binds to 0.0.0.0 and the port specified by the 'PORT' environment variable.
# GCP (Cloud Run, App Engine Flex) will provide PORT=8080 by default.
# For local Docker Compose, we'll set PORT to 8000.
CMD ["gunicorn", "myproject.wsgi:application", \
    "--bind", "0.0.0.0:${PORT}", \
    "--workers", "4", \
    "--worker-class", "gthread", \
    "--threads", "2", \
    "--access-logfile", "-", \
    "--error-logfile", "-"]