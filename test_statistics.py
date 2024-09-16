from unittest import TestCase
from statistics import variance, stdev, average
from math import sqrt


class AverageTest(TestCase):

    def test_average_typical_values(self):
        """Test average with typical integer and floating-point values."""
        self.assertEqual(3.0, average([1, 2, 3, 4, 5]))
        self.assertEqual(10.0, average([10, 10, 10, 10]))
        self.assertEqual(2.5, average([0, 1, 2, 3, 5, 4]))

    def test_average_negative_numbers(self):
        """Test average with negative values."""
        self.assertEqual(-3.0, average([-1, -2, -3, -4, -5]))
        self.assertAlmostEqual(-1.6666667, average([-1, 0, -4]))

    def test_average_mixed(self):
        """Test average with a mix of positive and negative values."""
        self.assertAlmostEqual(0.0, average([-5, -2, 2, 5]))
        self.assertAlmostEqual(1.25, average([-1, 0, 2, 4]))

    def test_average_non_integers(self):
        """Test average with decimal values."""
        self.assertAlmostEqual(2.05, average([1.0, 2.1, 3.05]))

    def test_average_single_value(self):
        """Average of a single value should return that value."""
        self.assertEqual(5.0, average([5]))

    def test_average_empty_list(self):
        """Average should raise ValueError for an empty list."""
        with self.assertRaises(ValueError):
            average([])


class VarianceTest(TestCase):

    def test_variance_typical_values(self):
        """variance of typical values"""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_non_integers(self):
        """variance should work with decimal values"""
        # variance([x,y,z]) == variance([x+d,y+d,z+d]) for any d
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]))
        # variance([0,4,4,8]) == 8
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]))

    def test_variance_identical_values(self):
        """Variance of identical values should be zero."""
        self.assertAlmostEqual(0.0, variance([5.5, 5.5, 5.5, 5.5]))

    def test_variance_negative_numbers(self):
        """Test variance with negative values."""
        self.assertAlmostEqual(2.0, variance([-1, -2, -3, -4, -5]))
        self.assertAlmostEqual(0.0, variance([-3, -3, -3]))

    def test_variance_mixed_signs(self):
        """Test variance with a mix of positive and negative values."""
        self.assertAlmostEqual(14.5, variance([-5, -2, 2, 5]))
        self.assertAlmostEqual(3.6875, variance([-1, 0, 2, 4]))

    def test_variance_single_value(self):
        """Variance of a single value should be zero."""
        self.assertAlmostEqual(0.0, variance([1]))

    def test_variance_empty_list(self):
        """Average should raise ValueError for an empty list."""
        with self.assertRaises(ValueError):
            variance([])


class StdevTest(TestCase):

    def test_stdev(self):
        # standard deviation of a single value should be zero
        self.assertEqual(0.0, stdev([10.0]))
        # simple test
        self.assertEqual(2.0, stdev([1, 5]))
        # variance([0, 0.5, 1, 1.5, 2.0]) is 0.5
        self.assertEqual(sqrt(0.5), stdev([0, 0.5, 1, 1.5, 2]))


if __name__ == '__main__':
    import unittest

    unittest.main(verbosity=1)
