FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set workdir directly to where the code will live
WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Copy requirements from the local backend folder
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

COPY . .

# Simplify the command: run main.py directly from the current folder
CMD ["uv", "run", "fastapi", "dev", "main.py", "--host", "0.0.0.0"]