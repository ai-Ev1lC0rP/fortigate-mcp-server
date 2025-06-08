# Dockerfile
FROM ghcr.io/astral-sh/uv:python3.11-alpine

WORKDIR /app


# Copy code
COPY . .

# Install dependencies
RUN uv sync


EXPOSE 8456

# Comando di avvio
CMD ["uv", "run", "python", "server.py"]