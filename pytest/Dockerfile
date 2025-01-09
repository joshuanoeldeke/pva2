# Use an official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install the time utility and other required tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    time && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint to run the tests
ENTRYPOINT ["./entrypoint.sh"]
