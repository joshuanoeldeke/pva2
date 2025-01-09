#!/bin/bash

# Ensure the logs directory exists
mkdir -p /app/logs

# Get the current date and time
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Run pytest and log resource usage
/usr/bin/time -v pytest -vvv test_app.py 2>&1 | tee /app/logs/test_metrics_$TIMESTAMP.log