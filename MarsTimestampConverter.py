class MarsTimestampConverter:
    def convert(self, hour: int, minute: int) -> int:
        """
        Converts a Mars-timestamp to total Mars-minutes since midnight.
        """
        total_minutes = hour * 100 + minute
        # Adjust total_minutes to be within 0 to 2500
        total_minutes %= 2500
        return total_minutes
