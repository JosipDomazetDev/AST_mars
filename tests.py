import unittest
from MarsTimestampConverter import MarsTimestampConverter
from IntervalNormalizer import IntervalNormalizer
from OverlapCalculator import OverlapCalculator
from TwilightRuleApplier import TwilightRuleApplier
from main import calculate_moon_overlap


class TestMarsOverlap(unittest.TestCase):

    def setUp(self):
        self.converter = MarsTimestampConverter()
        self.normalizer = IntervalNormalizer()
        self.calculator = OverlapCalculator()
        self.twilight = TwilightRuleApplier()

    # Equivalence Partitioning Tests

    def test_negative_input(self):
        """Test negative inputs for invalid data."""
        with self.assertRaises(ValueError):
            calculate_moon_overlap(-1, 0, 23, 59, 5, 0, 22, 0)

    def test_convert_midnight(self):
        """Test timestamp conversion at midnight."""
        result = self.converter.convert(0, 0)
        self.assertEqual(result, 0)

    def test_convert_full_day(self):
        """Test conversion of maximum valid input wrapping to zero."""
        result = self.converter.convert(25, 0)
        self.assertEqual(result, 0)

    def test_normalize_no_overlap(self):
        """Test interval normalization within a single day."""
        result = self.normalizer.normalize(300, 700)
        self.assertEqual(result, [(300, 700)])

    def test_calculate_no_overlap(self):
        """Test overlap calculation when intervals do not overlap."""
        intervals1 = [(500, 1000)]
        intervals2 = [(1200, 1500)]
        result = self.calculator.calculate_overlap(intervals1, intervals2)
        self.assertEqual(result, 0)

    def test_calculate_full_overlap(self):
        """Test overlap calculation for completely overlapping intervals."""
        intervals1 = [(500, 1000)]
        intervals2 = [(500, 1000)]
        result = self.calculator.calculate_overlap(intervals1, intervals2)
        self.assertEqual(result, 500)

    def test_twilight_no_overlap(self):
        """Test Twilight Rule application for non-overlapping intervals."""
        result = self.twilight.apply_twilight_rule(0, [(500, 1000)], [(1200, 1500)])
        self.assertEqual(result, 0)

    def test_calculate_moon_overlap_no_overlap(self):
        """Test full function for no overlap."""
        result = calculate_moon_overlap(0, 0, 1, 0, 2, 0, 3, 0)
        self.assertEqual(result, 0)

    def test_calculate_moon_overlap_full_overlap(self):
        """Test full function for fully overlapping intervals."""
        result = calculate_moon_overlap(5, 0, 6, 0, 5, 0, 6, 0)
        self.assertEqual(result, 100)

    # Boundary Value Analysis Tests

    def test_convert_wrap_around(self):
        """Test timestamp conversion at wrap-around boundary."""
        result = self.converter.convert(25, 15)
        self.assertEqual(result, 15)

    def test_normalize_wrap(self):
        """Test interval normalization with wrap-around."""
        result = self.normalizer.normalize(2300, 200)
        self.assertEqual(result, [(2300, 2500), (0, 200)])

    def test_normalize_full_day(self):
        """Test normalization for a full-day interval."""
        result = self.normalizer.normalize(600, 600)
        self.assertEqual(result, [(0, 2500)])

    def test_calculate_partial_overlap(self):
        """Test overlap calculation for partial overlaps."""
        intervals1 = [(500, 1000)]
        intervals2 = [(800, 1200)]
        result = self.calculator.calculate_overlap(intervals1, intervals2)
        self.assertEqual(result, 200)

    def test_twilight_single_point_overlap(self):
        """Test Twilight Rule for single-point overlap."""
        result = self.twilight.apply_twilight_rule(0, [(500, 1000)], [(1000, 1500)])
        self.assertEqual(result, 1)

    def test_twilight_multiple_intervals(self):
        """Test Twilight Rule with multiple interval scenarios."""
        result = self.twilight.apply_twilight_rule(0, [(2000, 2500), (0, 200)], [(2500, 300)])
        self.assertEqual(result, 1)

    def test_calculate_moon_overlap_partial_overlap(self):
        """Test full function for partially overlapping intervals."""
        result = calculate_moon_overlap(0, 30, 1, 30, 0, 45, 2, 0)
        self.assertEqual(result, 85)

    def test_calculate_moon_overlap_wrap_around(self):
        """Test full function for wrap-around intervals."""
        result = calculate_moon_overlap(23, 30, 0, 30, 23, 0, 1, 0)
        self.assertEqual(result, 200)


if __name__ == "__main__":
    unittest.main()
