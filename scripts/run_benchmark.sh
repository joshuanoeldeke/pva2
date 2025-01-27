#!/bin/bash

set -euo pipefail

# Create timestamp for logs/metrics
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Ensure results directory structure exists
rm -rf /app/results/*
mkdir -p /app/results/logs/{pytest,unittest} /app/results/metrics/{pytest,unittest}

# Run Pytest and capture logs/metrics in a single execution
echo "Running Pytest..."
/usr/bin/time -v -o "/app/results/metrics/pytest/pytest_time_${TIMESTAMP}.log" \
    pytest /app/tests/test_app_pytest.py \
    --junitxml="/app/results/logs/pytest/pytest_results_${TIMESTAMP}.xml" \
    --tb=long \
    -vvv 2>&1 | tee "/app/results/logs/pytest/pytest_${TIMESTAMP}.log"

# Run Unittest and capture logs/metrics in a single execution
echo "Running Unittest..."
/usr/bin/time -v -o "/app/results/metrics/unittest/unittest_time_${TIMESTAMP}.log" \
    python -m unittest discover -s /app/tests -p "test_app_unittest.py" \
    -v 2>&1 | tee "/app/results/logs/unittest/unittest_${TIMESTAMP}.log"

# Verify generated files are not empty
echo "Verifying generated files..."
find /app/results -type f | while read -r FILE; do
    if [[ ! -s "$FILE" ]]; then
        echo "ERROR: $FILE is empty or missing!"
        exit 1
    fi
done

echo "All tests completed successfully. Results saved in /app/results/"