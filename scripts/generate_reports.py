#!/usr/bin/env python3
import argparse
import os
import re
import csv
import json
import matplotlib.pyplot as plt
from xml.etree import ElementTree as ET
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def parse_unittest_log(log_path):
    """Parse Unittest log to get test execution times"""
    test_times = {}
    time_pattern = re.compile(r"Execution time for (\w+): (\d+\.\d+) seconds")

    with open(log_path) as f:
        for line in f:
            match = time_pattern.search(line)
            if match:
                test_name = match.group(1)
                duration = float(match.group(2))
                test_times[test_name] = duration
    return test_times


def parse_pytest_xml(xml_path):
    """Parse Pytest JUnit XML to get test durations"""
    tree = ET.parse(xml_path)
    root = tree.getroot()

    test_times = {}
    for testcase in root.findall(".//testcase"):
        test_name = testcase.get("name")
        duration = float(testcase.get("time"))
        test_times[test_name] = duration
    return test_times


def parse_metrics(metrics_path):
    """Parse time -v metrics file"""
    metrics = {}
    patterns = {
        "max_memory": r"Maximum resident set size \(kbytes\): (\d+)",
        "user_time": r"User time \(seconds\): (\d+\.\d+)",
        "system_time": r"System time \(seconds\): (\d+\.\d+)",
        "cpu_percent": r"Percent of CPU this job got: (\d+)%",
        "wall_clock": r"Elapsed \(wall clock\) time \(h:mm:ss or m:ss\): (.+)",
    }

    with open(metrics_path) as f:
        content = f.read()
        for key, pattern in patterns.items():
            match = re.search(pattern, content)
            if match:
                metrics[key] = match.group(1)
    return metrics


def generate_visualizations(data, timestamp, output_dir):
    """Generate matplotlib visualizations"""
    plt.style.use("ggplot")
    output_dir = Path(output_dir)

    # Test duration comparison
    frameworks = ["pytest", "unittest"]
    fig, ax = plt.subplots(figsize=(10, 6))

    for framework in frameworks:
        tests = data[framework]["tests"]
        names = list(tests.keys())
        durations = [t["duration"] for t in tests.values()]
        ax.barh(names, durations, alpha=0.6, label=framework)

    ax.set_xlabel("Execution Time (seconds)")
    ax.set_title("Test Duration Comparison")
    ax.legend()
    plt.tight_layout()
    plt.savefig(output_dir / f"duration_comparison_{timestamp}.png")
    plt.close()

    # System metrics comparison
    metrics = ["max_memory", "user_time", "system_time"]
    fig, ax = plt.subplots(figsize=(10, 6))

    for metric in metrics:
        values = [float(data[f][metric]) for f in frameworks]
        ax.bar(frameworks, values, alpha=0.6, label=metric)

    ax.set_ylabel("Value")
    ax.set_title("System Metrics Comparison")
    ax.legend()
    plt.tight_layout()
    plt.savefig(output_dir / f"system_metrics_{timestamp}.png")
    plt.close()


def generate_html_report(data, timestamp, output_dir):
    """Generate HTML report using Jinja2 template"""
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    report_path = Path(output_dir) / f"report_{timestamp}.html"
    with open(report_path, "w") as f:
        f.write(
            template.render(
                timestamp=timestamp,
                data=data,
                images=[
                    f"duration_comparison_{timestamp}.png",
                    f"system_metrics_{timestamp}.png",
                ],
            )
        )


def main():
    parser = argparse.ArgumentParser(description="Generate test reports")
    parser.add_argument("--timestamp", required=True, help="Test run timestamp")
    args = parser.parse_args()

    results_dir = Path("/app/results")
    raw_dir = results_dir / "raw"
    report_dir = results_dir / "reports"
    report_dir.mkdir(exist_ok=True)

    # Collect data
    data = {
        "pytest": {"tests": {}, "metrics": {}},
        "unittest": {"tests": {}, "metrics": {}},
    }

    # Process Pytest data
    pytest_prefix = f"pytest_{args.timestamp}"
    data["pytest"]["tests"] = parse_pytest_xml(raw_dir / f"{pytest_prefix}.xml")
    data["pytest"]["metrics"] = parse_metrics(raw_dir / f"{pytest_prefix}.metrics")

    # Process Unittest data
    unittest_prefix = f"unittest_{args.timestamp}"
    data["unittest"]["tests"] = parse_unittest_log(raw_dir / f"{unittest_prefix}.log")
    data["unittest"]["metrics"] = parse_metrics(raw_dir / f"{unittest_prefix}.metrics")

    # Generate outputs
    generate_visualizations(data, args.timestamp, report_dir)
    generate_html_report(data, args.timestamp, report_dir)

    # Save structured data
    with open(report_dir / f"benchmark_{args.timestamp}.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f"Generated reports in {report_dir}")


if __name__ == "__main__":
    main()
