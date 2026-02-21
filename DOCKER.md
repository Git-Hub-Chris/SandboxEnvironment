# Docker Setup for SandboxEnvironment

This repository includes Docker configuration for development, testing, and deployment.

## Quick Start

### Run Tests
```bash
docker-compose run test
```

### Interactive Development
```bash
docker-compose run dev
```
Then inside the container:
```bash
python calculator.py
pytest
ruff check .
black .
```

### Run Linting and Formatting
```bash
docker-compose run lint
```

## Build Images

Build the Docker image:
```bash
docker build -t sandbox:latest .
```

## Run Individual Services

### Test Service
```bash
docker-compose up test
```

### Development Service (Interactive)
```bash
docker-compose run -it dev bash
```

### Lint Service
```bash
docker-compose up lint
```

## Dockerfile Details

The Dockerfile uses a **multi-stage build**:
1. **Builder stage**: Installs Python dependencies
2. **Production stage**: Strips down to essentials, adds security (non-root user), and includes a health check

- Python 3.13-slim base image (minimal, ~150MB)
- Non-root user (`appuser`) for security
- Health check validates calculator functionality
- Default command runs pytest

## Docker Compose Services

| Service | Purpose |
|---------|---------|
| `dev` | Interactive development shell with mounted volumes |
| `test` | Runs pytest with verbose output |
| `lint` | Runs ruff, black, and other checks |

## Cleaning Up

Remove containers and images:
```bash
docker-compose down
docker image rm sandbox:latest
```

## Environment Variables

Set `PYTHONUNBUFFERED=1` to see real-time output from Python applications.

## Notes

- Volume mounts allow live code editing reflected in containers
- `__pycache__` is excluded to prevent host/container conflicts
- Multi-stage build reduces final image size
- Health check ensures application stability in production
