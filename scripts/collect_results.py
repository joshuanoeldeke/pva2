import json
import os


def process_pytest_metrics(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    print(f"Processed Pytest Metrics: {data}")


def process_unittest_logs(file_path):
    with open(file_path, "r") as f:
        logs = f.read()
    print(f"Processed Unittest Logs: {logs}")


if __name__ == "__main__":
    base_dir = "results"

    # Process Pytest Metrics
    pytest_metrics_path = os.path.join(base_dir, "metrics", "pytest_metrics.json")
    if os.path.exists(pytest_metrics_path):
        process_pytest_metrics(pytest_metrics_path)

    # Process Unittest Logs
    unittest_logs_path = os.path.join(base_dir, "logs", "unittest.log")
    if os.path.exists(unittest_logs_path):
        process_unittest_logs(unittest_logs_path)
