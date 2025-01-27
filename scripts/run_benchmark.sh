#!/bin/bash

# Create timestamp for logs/metrics
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Ensure results directory exists (and empty them if they already do)
rm -rf /app/results/*
mkdir -p /app/results/logs/pytest /app/results/logs/unittest
mkdir -p /app/results/metrics/pytest /app/results/metrics/unittest

# Run Pytest and save logs/metrics
echo "Running Pytest..."
pytest /app/tests/test_app_pytest.py \
    --junitxml=/app/results/logs/pytest/pytest_results_$TIMESTAMP.xml \
    --tb=long \
    -vvv 2>&1 | tee /app/results/logs/pytest/pytest_$TIMESTAMP.log

/usr/bin/time -v pytest /app/tests/test_app_pytest.py \
    -vvv 2>&1 | tee /app/results/metrics/pytest/pytest_time_$TIMESTAMP.log

# Run Unittest and save logs/metrics
echo "Running Unittest..."
python -m unittest discover -s /app/tests -p "test_app_unittest.py" \
    -v 2>&1 | tee /app/results/logs/unittest/unittest_$TIMESTAMP.log

/usr/bin/time -v python -m unittest discover -s /app/tests -p "test_app_unittest.py" \
    -v 2>&1 | tee /app/results/metrics/unittest/unittest_time_$TIMESTAMP.log

# Verify logs and metrics are generated
echo "Verifying generated files..."
for FILE in /app/results/logs/*/* /app/results/metrics/*/*; do
    if [ ! -s "$FILE" ]; then
        echo "WARNING: $FILE is empty or missing!"
    fi
done

echo "All tests completed. Results are saved in /app/results/"
