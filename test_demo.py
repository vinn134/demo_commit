from demo import calculate_mean
import unittest


class test_calculate_mean(unittest.TestCase):

    def test_lists(self):
        #self.assertEqual(calculate_mean([]), [])
        self.assertEqual(calculate_mean([10, 9]), 9.5)
        self.assertEqual(calculate_mean([10]), 10)

    def test_notValid(self):
        with self.assertRaises(ValueError):
            calculate_mean([])
