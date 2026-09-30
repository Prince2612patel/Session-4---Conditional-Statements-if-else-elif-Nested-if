# Task 2: Calculate grade based on marks (0-100)

marks = float(input("Enter your marks (0-100): "))

if 0 <= marks <= 100:

    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 40:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Invalid Input Plese Enter Valid Input")