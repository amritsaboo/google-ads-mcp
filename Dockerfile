FROM python:3.10-slim

# Prevent python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose standard HTTP port
ENV PORT=8000

WORKDIR /app

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Copy project files
COPY . .

# Install dependencies and the project
RUN pip install --no-cache-dir .

EXPOSE 8000

# The pyproject.toml defines "google-ads-mcp" as the script entrypoint
CMD ["google-ads-mcp"]
