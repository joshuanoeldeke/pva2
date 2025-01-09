#!/bin/bash

# Run pytest and log resource usage
/usr/bin/time -v pytest test_app.py 2>&1 | tee /app/logs/test_metrics.log