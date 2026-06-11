# Multi-stage build for production and development

# Stage 1: Builder
FROM python:3.14-slim@sha256:3fa9f1158b0d8b5029c357770bd522e7955546ffc5db885d8b366ec4a687afd4 AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Production
FROM python:3.14-slim@sha256:3fa9f1158b0d8b5029c357770bd522e7955546ffc5db885d8b366ec4a687afd4

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local

# Set PATH to include user bin
ENV PATH=/root/.local/bin:$PATH

# Copy application code
COPY my_package/calculator.py ./
COPY tests/test_calculator.py ./

# Create non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "from calculator import add; assert add(1,1)==2" || exit 1

# Default command runs tests
CMD ["pytest", "-v"]