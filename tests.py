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

    # Equivalence Partitioning: Testing the conversion of midnight timestamp.
    def test_convert_midnight(self):
        result = self.converter.convert(0, 0)
        self.assertEqual(result, 0)

    # Boundary Value Analysis: Testing wrap-around at 2500 Mars-minutes.
    def test_convert_wrap_around(self):
        result = self.converter.convert(25, 15)
        self.assertEqual(result, 15)

    # Equivalence Partitioning: Testing conversion of the maximum valid input.
    def test_convert_full_day(self):
        result = self.converter.convert(25, 0)
        self.assertEqual(result, 0)

    # Equivalence Partitioning: Testing normalization for intervals within a single day.
    def test_normalize_no_wrap(self):
        result = self.normalizer.normalize(300, 700)
        self.assertEqual(result, [(300, 700)])

    # Boundary Value Analysis: Testing normalization for wrap-around intervals.
    def test_normalize_wrap(self):
        result = self.normalizer.normalize(2300, 200)
        self.assertEqual(result, [(2300, 2500), (0, 200)])

    # Boundary Value Analysis: Testing normalization for a full-day interval.
    def test_normalize_full_day(self):
        result = self.normalizer.normalize(600, 600)
        self.assertEqual(result, [(0, 2500)])

    # Equivalence Partitioning: Testing overlap calculation when intervals do not overlap.
    def test_calculate_no_overlap(self):
        intervals1 = [(500, 1000)]
        intervals2 = [(1200, 1500)]
        result = self.calculator.calculate_overlap(intervals1, intervals2)
        self.assertEqual(result, 0)

    # Boundary Value Analysis: Testing overlap calculation for partial overlaps.
    def test_calculate_partial_overlap(self):
        intervals1 = [(500, 1000)]
        intervals2 = [(800, 1200)]
        result = self.calculator.calculate_overlap(intervals1, intervals2)
        self.assertEqual(result, 200)

    # Equivalence Partitioning: Testing overlap calculation for complete overlaps.
    def test_calculate_full_overlap(self):
        intervals1 = [(500, 1000)]
        intervals2 = [(500, 1000)]
        result = self.calculator.calculate_overlap(intervals1, intervals2)
        self.assertEqual(result, 500)

    # Equivalence Partitioning: Testing Twilight Rule application when no overlap exists.
    def test_twilight_no_overlap(self):
        result = self.twilight.apply_twilight_rule(0, [(500, 1000)], [(1200, 1500)])
        self.assertEqual(result, 0)

    # Boundary Value Analysis: Testing Twilight Rule for single-point overlap.
    def test_twilight_single_point_overlap(self):
        result = self.twilight.apply_twilight_rule(0, [(500, 1000)], [(1000, 1500)])
        self.assertEqual(result, 1)

    # Boundary Value Analysis: Testing Twilight Rule for multiple interval scenarios.
    def test_twilight_multiple_intervals(self):
        result = self.twilight.apply_twilight_rule(0, [(2000, 2500), (0, 200)], [(2500, 300)])
        self.assertEqual(result, 1)

    # Equivalence Partitioning: Testing no overlap for the main function.
    def test_calculate_moon_overlap_no_overlap(self):
        result = calculate_moon_overlap(0, 0, 1, 0, 2, 0, 3, 0)
        self.assertEqual(result, 0)

    # Boundary Value Analysis: Testing partial overlap for the main function.
    def test_calculate_moon_overlap_partial_overlap(self):
        result = calculate_moon_overlap(0, 30, 1, 30, 0, 45, 2, 0)
        self.assertEqual(result, 85)

    # Equivalence Partitioning: Testing full overlap for the main function.
    def test_calculate_moon_overlap_full_overlap(self):
        result = calculate_moon_overlap(5, 0, 6, 0, 5, 0, 6, 0)
        self.assertEqual(result, 100)

    # Boundary Value Analysis: Testing wrap-around intervals for the main function.
    def test_calculate_moon_overlap_wrap_around(self):
        result = calculate_moon_overlap(23, 30, 0, 30, 23, 0, 1, 0)
        self.assertEqual(result, 200)

if __name__ == "__main__":
    unittest.main()
