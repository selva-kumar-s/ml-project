def process_scores(students):
    """
    Task 1:
    """
    averages = {}
    for name, scores in students.items():
        if not scores:
            avg = 0.0  # fallback if an empty list appears
        else:
            avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg
    return averages


def classify_grades(averages):
    """
    Task 2:
    """
    # Thresholds (local variables as required)
    A_MIN = 90
    B_MIN = 75
    C_MIN = 60

    classified = {}
    for name, avg in averages.items():
        if avg >= A_MIN:
            grade = "A"
        elif avg >= B_MIN:
            grade = "B"
        elif avg >= C_MIN:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified


def generate_report(classified, passing_avg=70):
    """
    Task 3:
    """
    total_students = len(classified)
    passed = 0

    print("===== Student Grade Report =====")
    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed += 1

        # Name aligned to the left to match the example formatting
        print(f"{name:<9} | Avg: {avg:>5.2f} | Grade: {grade} | Status: {status}")

    failed = total_students - passed
    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")

    return passed


if __name__ == "__main__":
    # Example input that matches the sample report averages:
    students = {
        "Alice": [80, 90, 85, 90],
        "Bob":   [60, 65, 95, 85],
        "Clara": [95, 98, 97, 95],
    }

    averages = process_scores(students)          # Task 1
    classified = classify_grades(averages)       # Task 2
    passed_count = generate_report(classified)   # Task 3 (default passing_avg=70)