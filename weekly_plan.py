# CPT - Weekly Plan Generator
# Import these functions you made if you haven’t already
from workout_library import easy_run, tempo_run, long_run, interval_workout
from decision_rules import speed_work_allowed, recommend_focus

def generate_weekly_plan(weekly_miles, goal_race): # miles/goals as input
    plan = []
    focus = recommend_focus(goal_race)
    speed_ok = speed_work_allowed(weekly_miles)

    for day in range(1, 8):
        if day == 1:
            plan.append("Rest Day")

        elif day == 2:
            if speed_ok:
                plan.append(interval_workout(0))
            else:
                plan.append(easy_run(4))

        elif day == 3:
            plan.append(easy_run(5))

        elif day == 4:
            if focus == "speed":
                plan.append(tempo_run(4))
            else:
                plan.append(easy_run(4))

        elif day == 5:
            plan.append("Rest or Cross-Training")

        elif day == 6:
            plan.append(long_run(weekly_miles * 0.3))

        else:
            plan.append((easy_run(3)))
    return plan

week = generate_weekly_plan(30, "half")

print("\n--- WEEKLY TRAINING PLAN ---")
for day, workout in enumerate(week, start=1):
    print("Day", day, ":", workout)