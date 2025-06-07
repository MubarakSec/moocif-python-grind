# Write your solution here
def add_student(database:dict,name:str):
    if name not in database:
        database[name]=[]

def add_course(database:dict,name:str, course:tuple):
    course_name , grade = course
    if grade <= 0:
        return
    if name in database:
        i=0
        for exitsting_course in database[name]:
            exitsting_name,exitsting_grade = exitsting_course
            if exitsting_name == course_name:
                if grade > exitsting_grade:
                    database[name][i] = (course_name , grade)
                return
            i +=1
    database[name].append((course_name, grade))


def print_student(database:dict,name:str):
    if name not in database:
        print(f"{name}: no such person in the database")
    else:
        courses = database[name]
        print(f"{name}:")
        if not courses:
            print(" no completed courses")
        else:
            print(f" {len(courses)} completed courses:")
            total=0
            for course,garad in courses:
                print(f"  {course} {garad}")
                total+=garad
            average= total / len(courses)
            print(f" average grade {average:.1f}")


def summary(database: dict):
    num_student = len(database)
    print(f"students {num_student}")

    max_courses = -1
    student_most_courses = ""
    best_average = -1
    student_best_average = ""    

    for name, courses in database.items():
        if not courses:
            continue
        
        #counte courses
        num_courses=len(courses)
        if num_courses> max_courses:
            max_courses = num_courses
            student_most_courses = name
        
        #calculate avarage
        total = sum(grade for _, grade in courses)
        avarage = total/num_courses
        if avarage > best_average:
            best_average = avarage
            student_best_average = name


    print(f"most courses completed {max_courses} {student_most_courses}")
    print(f"best average grade {best_average:.1f} {student_best_average}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
