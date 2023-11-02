"""
Goal: Successfully manage data in one or more dictionaries, lists, tuples and/or variables

Assumptions:
1. Where possible, Python user-defined functions control the flow and execution of
the code

"""
courseInfo = {'course':'Intro to Programming', 'instructor': 'Dr Albert Einstein'}
grades = {'Allen':90, 'Barbara':92, 'Charles':80, 'Denise':85, 'Edward':74, 'Frances':80, 'Gary':60, 'Harry':94,
'Janice':91, 'Kelly':84, 'Larry':87}

grades['Mary'] = 100
grades['Nancy'] = 64
grades['Olivia'] = 88

student_names = []
student_grades = []

student_names = grades.keys()
student_grades = grades.values()

print(student_names)
print(student_grades)

def count_students():
    stu_ct = student_grades.count
    print("The number of students in the class is: ", stu_ct)

count_students()

"""
def count_students():
    student_number = ""
    for grade in grades.values():
        student_number += 1
        print(student_number)


    print(grades.keys())

count_students()

"""








