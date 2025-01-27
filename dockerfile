# Use an official Python image as a base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install the time utility and other required tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    time && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the scripts and test files
COPY . .

# Copy the requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Define a volume for the results files
VOLUME ["/app/results"]

# Default command
ENTRYPOINT ["scripts/entrypoint.sh"]