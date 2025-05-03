
import math

def gradingStudents(grades):
    for i in grades:
        if (5 * math.ceil(i/5))-i < 3 and i >= 38:
            print(5 * math.ceil(i/5))
        elif i < 38 or (5 * math.ceil(i/5))-i >= 3:
            print(i)


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
