# Task 4: Classify cricket team score

score = int(input("Enter cricket team score: "))

if score >= 200:
    print("High Score!")
elif score >= 150:
    print("Good Score")
elif score >= 100:
    print("Average")
else:
    print("Needs Improvement")

