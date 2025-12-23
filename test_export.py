from pt_planner.builder import build_plan
from pt_planner.export import export_plan_to_csv
from pt_planner.validate import validate_weekly_miles, validate_goal

def main():
    start_miles = 25
    goal = "half"

    validate_weekly_miles(start_miles)
    validate_goal(goal)

    plan = build_plan(start_miles, goal, weeks=8)
    export_plan_to_csv(plan, filename="training_plan.csv")

    print("Plan exported successfully to training_plan.csv")

if __name__ == "__main__":
    main()