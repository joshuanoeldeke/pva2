#!/bin/bash
set -euo pipefail

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
RESULTS_DIR="/app/results"
rm -rf "$RESULTS_DIR"/*
mkdir -p "$RESULTS_DIR/raw"

# Run Pytest and capture all data
echo "Running Pytest..."
/usr/bin/time -v -o "$RESULTS_DIR/raw/pytest_$TIMESTAMP.metrics" \
  pytest /app/tests/test_app_pytest.py \
    --junitxml="$RESULTS_DIR/raw/pytest_$TIMESTAMP.xml" \
    -vvv 2>&1 | tee "$RESULTS_DIR/raw/pytest_$TIMESTAMP.log"

# Run Unittest and capture all data
echo "Running Unittest..."
/usr/bin/time -v -o "$RESULTS_DIR/raw/unittest_$TIMESTAMP.metrics" \
  python -m unittest discover -s /app/tests -p "test_app_unittest.py" \
    -v 2>&1 | tee "$RESULTS_DIR/raw/unittest_$TIMESTAMP.log"

# Generate user-friendly reports
python /app/scripts/generate_reports.py --timestamp="$TIMESTAMP"

echo "All tests completed. Reports saved in $RESULTS_DIR/reports/"