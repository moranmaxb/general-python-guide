# LTC - Export and Load Training Plans

import csv


def export_plan_to_csv(plan, filename="training_plan.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Week", "Day", "Workout"])

        for week in plan:
            week_num = week["week"]
            for day_num, workout in enumerate(week["days"], start=1):
                writer.writerow([week_num, day_num, workout])


def load_plan_from_csv(filename="training_plan.csv"):
    plan = []
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            plan.append(row)
    return plan