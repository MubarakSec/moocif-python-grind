# Write your solution here
number=[]
while True:
        data=input("Exam points and exercises completed: ")
        if data == "":
            break
        number.append(list(map(int,data.split())))


total_points = []
grade=[0,0,0,0,0,0]
for i in number:
    exam=i[0]
    exercises=i[1]
    exercise_points = exercises // 10
    total = exam + exercise_points
    total_points.append(total)
    if i[0] < 10 or total <= 14:
        grade[0]+=1
        continue
    elif 15<= total <= 17:
        grade[1]+=1
    elif 18<= total <= 20:
        grade[2]+=1
    elif 21<= total <= 23:
        grade[3]+=1
    elif 24<= total <= 27:
        grade[4]+=1
    elif 28<= total <= 30:
        grade[5]+=1

total_students = sum(grade)
pass_count = sum(grade[1:])
pass_percentage = (pass_count / total_students) * 100
average=sum(total_points)/ len(total_points)
print("Statistics:")
print(f"Points average: {average:.1f}")
print(f"Pass percentage: {pass_percentage:.1f}")
print("Grade distribution:")
for i in range(len(grade)-1,-1,-1):

    print(f"{i}: {grade[i] * "*"}")

#the refactore version
'''
def parse_input():
    results = []
    while True:
        data = input("Exam points and exercises completed: ")
        if data == "":
            break
        results.append(list(map(int, data.split())))
    return results

def calculate_grade(exam, exercises):
    if exam < 10:
        return 0
    exercise_points = exercises // 10
    total = exam + exercise_points
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
    total_students = sum(grades)
    pass_count = sum(grades[1:])
    average = sum(total_points) / len(total_points)
    pass_percentage = (pass_count / total_students) * 100

    print("Statistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        print(f"{i}: {'*' * grades[i]}")

def main():
    data = parse_input()
    grades, total_points = compute_statistics(data)
    print_statistics(grades, total_points)

main()
'''
