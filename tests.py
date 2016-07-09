import unittest
from main import BinaryTime, Display


class TestBinaryTime(unittest.TestCase):
    @staticmethod
    def bin_time_to_matrix(bin_time: BinaryTime) -> list:
        return [
            bin_time.hour_tens,
            bin_time.hour_ones,
            bin_time.minute_tens,
            bin_time.minute_ones,
            bin_time.second_tens,
            bin_time.second_ones
        ]

    def test(self):
        bin_time1 = BinaryTime(0, 0, 0)
        bin_time2 = BinaryTime(20, 30, 45)
        bin_time3 = BinaryTime(12, 12, 30)

        bin_time1_mat = self.bin_time_to_matrix(bin_time1)
        bin_time2_mat = self.bin_time_to_matrix(bin_time2)
        bin_time3_mat = self.bin_time_to_matrix(bin_time3)

        #    1  2  4  8
        expected1 = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

        expected2 = [
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [1, 0, 1, 0],
        ]

        expected3 = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
        ]

        self.assertListEqual(
            bin_time1_mat,
            expected1
        )

        self.assertListEqual(
            bin_time2_mat,
            expected2
        )

        self.assertListEqual(
            bin_time3_mat,
            expected3
        )


class TestDisplay(unittest.TestCase):
    def test(self):
        display = Display()
        bin_time = BinaryTime(12, 1, 13)

        bin_str = display.bin_time_to_str(bin_time)

        expected_bin_str = \
            "[ ][ ][ ][ ][ ][ ]\n" \
            "[ ][ ][ ][ ][ ][ ]\n" \
            "[ ][X][ ][ ][ ][X]\n" \
            "[X][ ][ ][X][X][X]\n"

        self.assertEqual(
            bin_str,
            expected_bin_str
        )

if __name__ == '__main__':
    unittest.main()
