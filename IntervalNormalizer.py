class IntervalNormalizer:
    def normalize(self, start: int, end: int) -> list:
        """
        Normalizes Mars-intervals to handle intervals that may wrap around the day boundary.
        Returns a list of intervals.
        """
        if start == end:
            # Full day interval
            return [(0, 2500)]
        elif start < end:
            # Interval does not wrap around
            return [(start, end)]
        else:
            # Interval wraps around
            return [(start, 2500), (0, end)]
