# Use the official uv image for Python 3.12
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Enable bytecode compilation for faster startup
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Copy dependency files first to use Docker's cache
COPY pyproject.toml uv.lock ./

# Install dependencies without installing the project itself yet
RUN uv sync --frozen --no-install-project

# Copy the rest of your backend code
COPY . .

# Start FastAPI in development mode
CMD ["uv", "run", "fastapi", "dev", "--host", "0.0.0.0", "backend/main.py"]