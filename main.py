from MarsTimestampConverter import MarsTimestampConverter
from IntervalNormalizer import IntervalNormalizer
from OverlapCalculator import OverlapCalculator
from TwilightRuleApplier import TwilightRuleApplier

def calculate_moon_overlap(
    D_rise_h: int, D_rise_m: int, D_set_h: int, D_set_m: int,
    P_rise_h: int, P_rise_m: int, P_set_h: int, P_set_m: int
) -> int:
    """
    Calculates the time both moons are jointly visible.
    """
    # Instantiate components
    converter = MarsTimestampConverter()
    normalizer = IntervalNormalizer()
    calculator = OverlapCalculator()
    twilight = TwilightRuleApplier()

    # Convert timestamps to total minutes
    D_rise = converter.convert(D_rise_h, D_rise_m)
    D_set = converter.convert(D_set_h, D_set_m)
    P_rise = converter.convert(P_rise_h, P_rise_m)
    P_set = converter.convert(P_set_h, P_set_m)

    # Normalize intervals
    D_intervals = normalizer.normalize(D_rise, D_set)
    P_intervals = normalizer.normalize(P_rise, P_set)

    # Calculate overlap
    initial_overlap = calculator.calculate_overlap(D_intervals, P_intervals)

    # Apply Twilight Rule
    final_overlap = twilight.apply_twilight_rule(
        initial_overlap, D_intervals, P_intervals
    )

    return final_overlap

if __name__ == "__main__":
    # Example input: D[24:53, 7:12] P[5:12, 8:45]
    D_rise_h, D_rise_m = 24, 53
    D_set_h, D_set_m = 7, 12
    P_rise_h, P_rise_m = 5, 12
    P_set_h, P_set_m = 8, 45

    D_rise_h, D_rise_m = 13, 91
    D_set_h, D_set_m = 23, 5
    P_rise_h, P_rise_m = 22, 5
    P_set_h, P_set_m = 24, 45

    # D_rise_h, D_rise_m = 22, 11
    # D_set_h, D_set_m = 0, 36
    # P_rise_h, P_rise_m = 7, 0
    # P_set_h, P_set_m = 22, 11

    overlap = calculate_moon_overlap(
        D_rise_h, D_rise_m, D_set_h, D_set_m,
        P_rise_h, P_rise_m, P_set_h, P_set_m
    )

    print(f"The moons are jointly visible for {overlap} Mars-minutes.")
