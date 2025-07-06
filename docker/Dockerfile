# Multi-stage build for DevSpace
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    libffi-dev \
    libssl-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd --gid 1000 devspace && \
    useradd --uid 1000 --gid devspace --shell /bin/bash --create-home devspace

# Set work directory
WORKDIR /app

# Copy requirements
COPY pyproject.toml ./
COPY requirements*.txt* ./

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -e .

# Development stage
FROM base as development

# Install development dependencies
RUN pip install -e ".[dev,ml,robotics]"

# Copy application code
COPY --chown=devspace:devspace . .

# Create necessary directories
RUN mkdir -p /app/logs /app/data /app/data/models && \
    chown -R devspace:devspace /app

# Switch to non-root user
USER devspace

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Default command
CMD ["python", "-m", "uvicorn", "app.http.main:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]

# Production stage
FROM base as production

# Install only production dependencies
RUN pip install -e ".[ml,robotics]"

# Copy application code
COPY --chown=devspace:devspace app ./app
COPY --chown=devspace:devspace config ./config
COPY --chown=devspace:devspace pyproject.toml ./
COPY --chown=devspace:devspace README.md ./

# Create necessary directories
RUN mkdir -p /app/logs /app/data /app/data/models && \
    chown -R devspace:devspace /app

# Switch to non-root user
USER devspace

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Default command for production
CMD ["python", "-m", "uvicorn", "app.http.main:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
