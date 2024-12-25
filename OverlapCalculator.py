class OverlapCalculator:
    def calculate_overlap(self, intervals1: list, intervals2: list) -> int:
        """
        Calculates the total overlap duration between two lists of intervals.
        """
        total_overlap = 0
        for int1 in intervals1:
            for int2 in intervals2:
                overlap = self._compute_interval_overlap(int1, int2)
                total_overlap += overlap
        return total_overlap

    def _compute_interval_overlap(self, interval1: tuple, interval2: tuple) -> int:
        """
        Computes overlap between two intervals.
        """
        start_overlap = max(interval1[0], interval2[0])
        end_overlap = min(interval1[1], interval2[1])
        overlap = max(0, end_overlap - start_overlap)
        return overlap
