import time

def add(a, b):
    time.sleep(0.01)  # Simulate workload
    return a + b

def test_add_benchmark(benchmark):
    result = benchmark(add, 2, 3)
    assert result == 5