import time
from app import add


def test_add():
    start_time = time.time()
    result = add(2, 3)
    assert result == 5
    end_time = time.time()
    execution_time = end_time - start_time
    with open("test_metrics.log", "a") as log_file:
        log_file.write(f"test_add executed in {execution_time:.6f} seconds\n")