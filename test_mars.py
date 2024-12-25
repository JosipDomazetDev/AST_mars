import unittest

from main import calculate_moon_overlap


class TestCalculateMoonOverlap(unittest.TestCase):

    # Equivalence Partitioning Tests

    def test_negative_input(self):
        """Test negative inputs for invalid data.
        Equivalence Partition: Invalid input where negative values are not allowed.
        """
        with self.assertRaises(ValueError):
            calculate_moon_overlap(-1, 0, 23, 99, 5, 0, 22, 99)

    def test_no_overlap(self):
        """Test when intervals do not overlap at all.
        Equivalence Partition: Non-overlapping intervals.
        """
        result = calculate_moon_overlap(0, 0, 1, 0, 2, 0, 3, 0)
        self.assertEqual(result, 0)

    def test_full_overlap(self):
        """Test when one interval completely overlaps the other.
        Equivalence Partition: Full overlap of one interval within the other.
        """
        result = calculate_moon_overlap(5, 0, 6, 0, 5, 0, 6, 0)
        self.assertEqual(result, 100)

    def test_partial_overlap_start(self):
        """Test when intervals partially overlap at the start.
        Equivalence Partition: Partial overlap at the start of one interval.
        """
        result = calculate_moon_overlap(5, 0, 6, 0, 5, 50, 6, 50)
        self.assertEqual(result, 50)

    def test_partial_overlap_end(self):
        """Test when intervals partially overlap at the end.
        Equivalence Partition: Partial overlap at the end of one interval.
        """
        result = calculate_moon_overlap(4, 50, 6, 0, 5, 0, 6, 50)
        self.assertEqual(result, 100)

    def test_disjoint_intervals(self):
        """Test disjoint intervals with no overlap.
        Equivalence Partition: Completely disjoint intervals.
        """
        result = calculate_moon_overlap(5, 0, 6, 0, 7, 0, 8, 0)
        self.assertEqual(result, 0)

    def test_overlap_wraparound(self):
        """Test intervals that wrap around midnight with overlap.
        Equivalence Partition: Intervals spanning midnight with overlap.
        """
        result = calculate_moon_overlap(23, 50, 0, 50, 23, 0, 1, 0)
        self.assertEqual(result, 200)

    def test_no_overlap_wraparound(self):
        """Test intervals that wrap around midnight without overlap.
        Equivalence Partition: Intervals spanning midnight without overlap.
        """
        result = calculate_moon_overlap(23, 50, 0, 50, 1, 0, 2, 0)
        self.assertEqual(result, 0)

    def test_full_day_overlap(self):
        """Test intervals covering a full day.
        Equivalence Partition: Intervals spanning the entire Mars day.
        """
        result = calculate_moon_overlap(0, 0, 25, 0, 0, 0, 25, 0)
        self.assertEqual(result, 2500)

    def test_single_point_overlap(self):
        """Test when intervals overlap at a single point.
        Equivalence Partition: Single-point overlap due to the Twilight Rule.
        """
        result = calculate_moon_overlap(5, 0, 6, 0, 6, 0, 7, 0)
        self.assertEqual(result, 1)

    # Boundary Value Analysis Tests

    def test_start_boundary(self):
        """Test overlap at the start boundary.
        Boundary Value: Overlap starting at the boundary of the first interval.
        """
        result = calculate_moon_overlap(0, 0, 1, 0, 0, 50, 1, 50)
        self.assertEqual(result, 50)

    def test_end_boundary(self):
        """Test overlap at the end boundary.
        Boundary Value: Overlap ending at the boundary of the first interval.
        """
        result = calculate_moon_overlap(23, 0, 24, 0, 22, 50, 23, 50)
        self.assertEqual(result, 50)

    def test_minimum_interval_overlap(self):
        """Test the smallest possible overlapping interval.
        Boundary Value: Smallest overlap of 1 Mars-minute.
        """
        result = calculate_moon_overlap(5, 99, 6, 0, 5, 99, 6, 0)
        self.assertEqual(result, 1)

    def test_large_interval_overlap(self):
        """Test a large overlap near the maximum time range.
        Boundary Value: Large overlap near the maximum valid time range.
        """
        result = calculate_moon_overlap(20, 0, 25, 0, 21, 0, 24, 0)
        self.assertEqual(result, 300)

    def test_edge_case_midnight(self):
        """Test intervals that overlap exactly at midnight.
        Boundary Value: Overlap exactly at Mars midnight.
        """
        result = calculate_moon_overlap(23, 99, 1, 0, 0, 0, 1, 0)
        self.assertEqual(result, 100)


if __name__ == "__main__":
    unittest.main()
