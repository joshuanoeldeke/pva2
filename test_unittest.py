import unittest
import time
from sample_code import add, multiply


class TestSampleCode(unittest.TestCase):
    def test_add(self):
        start_time = time.time()
        for _ in range(100000):
            self.assertEqual(add(2, 3), 5)
        end_time = time.time()
        print(f"Execution time for test_add: {end_time - start_time} seconds")

    def test_multiply(self):
        start_time = time.time()
        for _ in range(100000):
            self.assertEqual(multiply(2, 3), 6)
        end_time = time.time()
        print(f"Execution time for test_multiply: {end_time - start_time} seconds")

class TestSampleCode2(unittest.TestCase):
    def test_add_2(self):
        start_time = time.time()
        for _ in range(100000):
            self.assertEqual(add(2, 3), 2+3)
        end_time = time.time()
        print(f"Execution time for test_add_2: {end_time - start_time} seconds")

    def test_multiply_2(self):
        start_time = time.time()
        for _ in range(100000):
            self.assertEqual(multiply(2, 3), 2*3)
        end_time = time.time()
        print(f"Execution time for test_multiply_2: {end_time - start_time} seconds")

if __name__ == "__main__":
    unittest.main()
