import pytest
from sample_code import add, multiply


# Benchmarking the add function
def test_add(benchmark):
    result = benchmark(lambda: add(2, 3))
    assert result == 5


# Benchmarking the multiply function
def test_multiply(benchmark):
    result = benchmark(lambda: multiply(2, 3))
    assert result == 6


# Alternative benchmark tests
def test_add_2(benchmark):
    result = benchmark(lambda: add(2, 3))
    assert result == 2 + 3


def test_multiply_2(benchmark):
    result = benchmark(lambda: multiply(2, 3))
    assert result == 2 * 3
