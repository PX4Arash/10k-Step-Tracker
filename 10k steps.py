GOAL_STEPS = 10_000

total_steps = 0
days = 0

print("🏃 Welcome to the 10K Step Tracker!")
print(f"🎯 Your daily goal: {GOAL_STEPS:,} steps\n")

while total_steps < GOAL_STEPS:
    steps = int(input("Enter your steps for today: "))

    if steps < 0:
        print("❌ Steps cannot be negative!\n")
        continue

    total_steps += steps
    days += 1

    remaining_steps = GOAL_STEPS - total_steps

    if remaining_steps > 0:
        print(
            f"📊 {remaining_steps:,} steps remaining "
            f"to reach the goal.\n"
        )
    else:
        print(
            f"🎉 Congratulations! You reached {GOAL_STEPS:,} steps "
            f"after {days} day(s)!"
        )