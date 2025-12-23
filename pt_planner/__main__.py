# COL - Main Command Entry

from .builder import build_plan
from .export import export_plan_to_csv
from .validate import validate_weekly_miles, validate_goal


def main():
    start_miles = 25
    goal = "half"
    weeks = 12

    validate_weekly_miles(start_miles)
    validate_goal(goal)

    plan = build_plan(start_miles, goal, weeks)
    export_plan_to_csv(plan)

    print("Training plan generated and exported successfully.")


if __name__ == "__main__":
    main()