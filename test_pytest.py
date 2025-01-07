import time
from sample_code import add, multiply


# Test for add function
def test_add():
    start_time = time.time()
    for _ in range(100000):
        assert add(2, 3) == 5
    end_time = time.time()
    print(f"Execution time for test_add: {end_time - start_time} seconds")


# Test for multiply function
def test_multiply():
    start_time = time.time()
    for _ in range(100000):
        assert multiply(2, 3) == 6
    end_time = time.time()
    print(f"Execution time for test_multiply: {end_time - start_time} seconds")


# Alternative tests with different expected values
def test_add_2():
    start_time = time.time()
    for _ in range(100000):
        assert add(2, 3) == 2 + 3
    end_time = time.time()
    print(f"Execution time for test_add_2: {end_time - start_time} seconds")


def test_multiply_2():
    start_time = time.time()
    for _ in range(100000):
        assert multiply(2, 3) == 2 * 3
    end_time = time.time()
    print(f"Execution time for test_multiply_2: {end_time - start_time} seconds")
