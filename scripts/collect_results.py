import os
import matplotlib.pyplot as plt


def extract_metrics(results_dir):
    metrics = {}
    for framework in ["pytest", "unittest"]:
        log_file = os.path.join(results_dir, framework, f"{framework}_time.log")
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                for line in f:
                    if "User time (seconds):" in line:
                        metrics[framework] = float(line.split(":")[-1].strip())
        else:
            print(f"Time log for {framework} not found.")
    return metrics


def visualize_metrics(metrics):
    frameworks = list(metrics.keys())
    times = list(metrics.values())

    plt.bar(frameworks, times, color=["blue", "green"])
    plt.xlabel("Framework")
    plt.ylabel("Execution Time (s)")
    plt.title("Test Execution Time by Framework")
    plt.savefig("execution_times.png")
    plt.show()


if __name__ == "__main__":
    results_directory = "/app/results"
    metrics = extract_metrics(results_directory)
    if metrics:
        visualize_metrics(metrics)
    else:
        print("No metrics found to visualize.")
