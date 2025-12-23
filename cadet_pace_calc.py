# West Point Cadet - Pace Calculator

# Get user input
distance = float(input("Enter distance in miles: "))
time_minutes = float(input("Enter total time in minutes: "))

# Calculate pace
pace = time_minutes/ distance

# Display result
print("\n--- PACE REPORT ---")
print("Distance:", distance, "miles")
print("Time:", time_minutes, "minutes")
print("Average pace:", round(pace, 2), "minutes per mile")

print("\n--- MILE SPLITS ---")

mile = 1
while mile <= int(distance):
    print("Mile", mile, ":", round(pace * mile, 2), "minutes")
    mile = mile + 1