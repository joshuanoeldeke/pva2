#!/bin/bash

# Run pytest and log resource usage
/usr/bin/time -v pytest test_app.py 2>&1 | tee -a test_metrics.log