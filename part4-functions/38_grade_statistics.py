def parse_input():
    """Collects input and returns a list of (exam, exercises) tuples."""
    results = []
    while True:
        try:
            data = input("press enter to quit. Exam points and exercises completed: ")
            if data == "":
                break
            parts = list(map(int, data.strip().split()))
            if len(parts) != 2 or not (0 <= parts[0] <= 30) or not (0 <= parts[1] <= 100):
                print("Invalid input. Please enter two integers: exam points (0-30) and exercises (0-100).")
                continue
            results.append((parts[0], parts[1]))
        except ValueError:
            print("Invalid input. Enter two integers separated by space.")
    return results


def calculate_grade(exam, exercises):
    """Calculates grade based on rules."""
    if exam < 10:
        return 0
    total = exam + (exercises // 10)
    if total <= 14:
        return 0
    elif total <= 17:
        return 1
    elif total <= 20:
        return 2
    elif total <= 23:
        return 3
    elif total <= 27:
        return 4
    else:
        return 5


def compute_statistics(data):
    """Processes data and returns grade distribution and total points."""
    grades = [0] * 6
    total_points = []

    for exam, exercises in data:
        exercise_points = exercises // 10
        total = exam + exercise_points
        total_points.append(total)
        grade = calculate_grade(exam, exercises)
        grades[grade] += 1

    return grades, total_points


def print_statistics(grades, total_points):
    """Prints average, pass percentage, and grade distribution."""
    total_students = sum(grades)
    if total_students == 0:
        print("No data to process.")
        return

    pass_count = sum(grades[1:])
    average = sum(total_points) / total_students
    pass_percentage = (pass_count / total_students) * 100

    print("Statistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        print(f"{i}: {'*' * grades[i]}")


def main():
    data = parse_input()
    if not data:
        print("No input provided.")
        return
    grades, total_points = compute_statistics(data)
    print_statistics(grades, total_points)


if __name__ == "__main__":
    main()
