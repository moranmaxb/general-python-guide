# BG - Adaptive Risk Analysis

def calculate_ramp_rate(prev_miles, current_miles):
    """
    Calculates week-to-week mileage increase percentage.
    """
    if prev_miles == 0:
        return 0
    return (current_miles - prev_miles) / prev_miles


def ramp_rate_warning(prev_miles, current_miles):
    rate = calculate_ramp_rate(prev_miles, current_miles)

    if rate > 0.10:
        return True, round(rate * 100, 1)
    else:
        return False, round(rate * 100, 1)
    
def fatigue_score(week_plan):
    score = 0

    for workout in week_plan:
        if workout is None:
            continue
        text = workout.lower()

        if "rest" in text:
            score += 0
        elif "interval" in text or "tempo" in text:
            score += 3
        elif "long run" in text:
            score += 4
        else:
            score += 1

    return score

def adaptive_adjustment(prev_week, current_week):
    warnings = []

    ramp_flag, ramp_pct = ramp_rate_warning(
        prev_week["weekly_miles"],
        current_week["weekly_miles"]
    )

    fatigue = fatigue_score(current_week["days"])

    if ramp_flag:
        warnings.append(f"Ramp rate high: {ramp_pct}%")

    if fatigue > 15:
        warnings.append(f"High fatigue score: {fatigue}")

    return warnings

if __name__ == "__main__":
    from .builder import build_plan

    plan = build_plan(25, "half", weeks=6)

    for i in range(1, len(plan)):
        warnings = adaptive_adjustment(plan[i-1], plan[i])
        if warnings:
            print(f"\nWARNING - WEEK {plan[i]['week']} WARNINGS:")
            for w in warnings:
                print("-", w)