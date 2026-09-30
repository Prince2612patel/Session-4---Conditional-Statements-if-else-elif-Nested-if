# Task 3: Check late night food ordering using nested if statements
# Conditions: Age >= 18 and Time between 22 (10 PM) and 2 (2 AM)

age = int(input("Enter your age: "))
time = int(input("Enter current time in 24-hour format (0-23): "))

if age >= 18:
    # Nested check for late-night time window crossing midnight
    if time >= 22 or time <= 2:
        print("Order allowed")
    else:
        print("Order not allowed")
else:
    print("Order not allowed")