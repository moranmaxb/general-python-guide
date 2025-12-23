# MAJ - Multi-Week Plan Builder

from weekly_plan import generate_weekly_plan

def apply_cutback(weekly_miles):
    # reduce volume to recover
    return weekly_miles * 0.80

def apply_build(weekly_miles, build_rate=0.08):
    # increase volume for progression
    return weekly_miles * (1 + build_rate)

def apply_taper(weekly_miles, taper_factor):
    return weekly_miles * taper_factor

def build_plan(start_weekly_miles, goal_race, weeks=12):
    all_weeks = []
    weekly_miles = float(start_weekly_miles)

    for week_num in range(1, weeks + 1):
        # Cutback every 4th week (except if it's in taper)
        in_taper = (week_num >= weeks - 1)

        if in_taper:
            # two-week taper
            if week_num == weeks - 1:
                weekly_miles = apply_taper(weekly_miles, 0.70)
            else:
                weekly_miles = apply_taper(weekly_miles, 0.50)

        elif week_num % 4 == 0:
            weekly_miles = apply_cutback(weekly_miles)

        else:
            # normal build week (except week 1)
            if week_num != 1:
                weekly_miles = apply_build(weekly_miles, build_rate=0.08)

        week_plan = generate_weekly_plan(weekly_miles, goal_race)
        all_weeks.append({
            "week": week_num,
            "weekly_miles": round(weekly_miles, 1),
            "days": week_plan
        })

    return all_weeks

plan = build_plan(start_weekly_miles=25, goal_race="half", weeks=12)

for w in plan:
    print("\n==========================")
    print("WEEK", w["week"], "| Target Miles:", w["weekly_miles"])
    print("==========================")
    for day_num, workout in enumerate(w["days"], start=1):
        print("Day", day_num, ":", workout)