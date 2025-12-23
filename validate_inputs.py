# LTC - Input Validation

def validate_weekly_miles(miles):
    if miles <= 0:
        raise ValueError("Weekly mileage must be positive.")
    if miles > 120:
        raise ValueError("Weekly mileage exceeds safe limits.")
    return True


def validate_goal(goal):
    valid_goals = ["5k", "10k", "half", "marathon"]
    if goal not in valid_goals:
        raise ValueError(f"Goal must be one of {valid_goals}.")
    return True