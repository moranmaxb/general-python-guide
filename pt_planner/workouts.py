def easy_run():
    print("Easy Run")
    print("Distance: 4 miles")
    print("Pace: Comfortable, conversational")

easy_run()

def easy_run(distance):
    print("Easy Run")
    print("Distance:", distance, "miles")
    print("Pace: Comfortable")

interval_workouts = [
    "6 x 400m fast, 200m jog",
    "4 x 800m at 5K pace",
    "3 x 1 mile at threshold"
]

print(interval_workouts[0])

# 2LT - Workout Library

def easy_run(distance):
    return f"Easy Run: {distance} miles at comfortable pace"

def tempo_run(distance):
    return f"Tempo Run: {distance} miles at controlled hard pace"

def long_run(distance):
    return f"Long Run: {distance} miles, slow and steady"

interval_workouts = [
    "6 x 400m fast, 200m jog",
    "4 x 800m at 5K pace",
    "3 x 1 mile at threshold"
]

def interval_workout(choice):
    return interval_workouts[choice]

print(easy_run(4))
print(tempo_run(5))
print(long_run(10))
print("Intervals:", interval_workout(2))