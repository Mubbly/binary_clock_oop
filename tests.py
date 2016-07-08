import unittest
from main import BinaryTime
from datetime import datetime


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class TestBinaryTime(unittest.TestCase):
    def test(self):
        time1 = datetime(hour=0, minute=0, second=0)
        time2 = datetime(hour=20, minute=30, second=45)

        bin_time1 = BinaryTime(time1)

        self.assertEqual(
            bin_time1.hour_ones,
            [0, 0, 0, 0]
        )

if __name__ == '__main__':
    unittest.main()
