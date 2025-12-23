weekly_miles = 30

if weekly_miles < 20:
    print("Low mileage week")
elif weekly_miles < 40:
    print("Moderate mileage week")
else:
    print("High mileage week")

# 1LT - Decision Rules Engine

def classify_mileage(weekly_miles):
    if weekly_miles < 20:
        return "low"
    elif weekly_miles < 40:
        return "moderate"
    else:
        return "high"

def speed_work_allowed(weekly_miles):
    if weekly_miles < 15:
        return False
    else:
        return True

def recommend_focus(goal_race):
    if goal_race == "5k":
        return "speed"
    elif goal_race == "10k":
        return "balanced"
    elif goal_race == "half":
        return "endurance"
    elif goal_race == "marathon":
        return "long_run"
    else:
        return "general_fitness"
    
miles = 30
goal = "half"

print("Mileage class:", classify_mileage(miles))
print("Speed work allowed:", speed_work_allowed(miles))
print("Training focus:", recommend_focus(goal))