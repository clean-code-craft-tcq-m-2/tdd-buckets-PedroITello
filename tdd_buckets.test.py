import unittest

import tdd_buckets as tddb
import tdd_12_bit_conversor as tdd12b
import tdd_10_bit_conversor as tdd10b
import tdd_buckets_constants as tddbc


class TDDTest(unittest.TestCase):

  def test_check_and_alert(self):
    self.assertEqual(
      tddb.check_ranges_on_array(
        tddbc.TEST_ARRAY_THREE
      ), [["4-5", 2]]
    )

  def test_12_bit_conversor(self):

    self.assertEqual(
      tdd12b.read_12_bit_input(
        900
      ), 2
    )

    self.assertEqual(
      tdd12b.read_12_bit_input(
        1146
      ), 3
    )

    self.assertEqual(
      tdd12b.read_12_bit_input(
        4095
      ), "ERROR"
    )

  def test_10_bit_conversor(self):

    self.assertEqual(
      tdd10b.read_10_bit_input(
        1022, -15, 15
      ), 15
    )

    self.assertEqual(
      tdd10b.read_10_bit_input(
        0, -12, 12
      ), -12
    )

    self.assertEqual(
      tdd10b.read_10_bit_input(
        511, -15, 15
      ), "NOT CURRENT"
    )


if __name__ == '__main__':
  unittest.main()
