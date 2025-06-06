# Stage 1: Builder
FROM python:3.11-slim-bullseye AS builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# --- MODIFIED SECTION FOR TORCH ---
# Add the manually downloaded torch wheel file to the build context
# Ensure this file is in the same directory as your Dockerfile
ADD torch-2.7.0-cp311-cp311-manylinux_2_28_x86_64.whl .

# Install torch from the local wheel file
RUN pip install --no-cache-dir ./torch-2.7.0-cp311-cp311-manylinux_2_28_x86_64.whl

# Copy the modified requirements.txt (which no longer contains torch)
COPY requirements.txt .

# Upgrade pip and then install the rest of the Python dependencies from requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
# --- END MODIFIED SECTION ---

# Stage 2: Runtime
FROM python:3.11-slim-bullseye

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq5 \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Copy virtual environment
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Create non-root user
RUN useradd -m appuser && \
    mkdir -p /app/static /app/media && \
    chown -R appuser:appuser /app
USER appuser

# Copy application
COPY --chown=appuser:appuser . .

# Fix line endings and permissions
RUN sed -i 's/\r$//' docker-entrypoint.sh && \
    chmod +x docker-entrypoint.sh

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=myproject.settings

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1

# Entrypoint
ENTRYPOINT ["./docker-entrypoint.sh"]

# Default command
CMD ["gunicorn", "myproject.wsgi:application", \
    "--bind", "0.0.0.0:8000", \
    "--workers", "4", \
    "--worker-class", "gthread", \
    "--threads", "2", \
    "--access-logfile", "-", \
    "--error-logfile", "-"]
