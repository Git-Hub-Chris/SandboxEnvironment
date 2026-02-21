# Multi-stage build for production and development

# Stage 1: Builder
FROM python:3.14-slim as builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Production
FROM python:3.14-slim

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local

# Set PATH to include user bin
ENV PATH=/root/.local/bin:$PATH

# Copy application code
COPY calculator.py hello.py ./
COPY test_calculator.py test_hello.py ./

# Create non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "from calculator import add; assert add(1,1)==2" || exit 1

# Default command runs tests
CMD ["pytest", "-v"]
