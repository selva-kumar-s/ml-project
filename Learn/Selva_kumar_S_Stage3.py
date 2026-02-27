# Stage 3: Student Grade Calculator

name = input("Enter student name: ")
m1 = int(input("Enter mark 1 (0-100): "))
m2 = int(input("Enter mark 2 (0-100): "))
m3 = int(input("Enter mark 3 (0-100): "))

# Optional: validate marks range
if (m1 < 0 or m1 > 100) or (m2 < 0 or m2 > 100) or (m3 < 0 or m3 > 100):
    print("Error: Marks must be between 0 and 100.")
else:
    total = m1 + m2 + m3
    percentage = (total / 300) * 100

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"

    print("\n" + name)
    print(f"Total: {int(total)}/300" if total.is_integer() else f"Total: {total}/300")
    print(f"Percentage: {percentage:.1f}%")
    print("Grade:", grade)
