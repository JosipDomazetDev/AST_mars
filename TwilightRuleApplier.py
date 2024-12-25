class TwilightRuleApplier:
    def apply_twilight_rule(self, overlap: int, intervals1: list, intervals2: list) -> int:
        """
        Applies the Twilight Rule when intervals share only a single point.
        """
        if overlap > 0:
            return overlap

        # Check for single-point overlaps
        points1 = {interval[0] for interval in intervals1} | {interval[1] for interval in intervals1}
        points2 = {interval[0] for interval in intervals2} | {interval[1] for interval in intervals2}
        common_points = points1 & points2

        if common_points:
            return 1  # Twilight Rule applies

        return 0
