def gradingStudents(grades):
    for grade in grades:
        if grade > 37:
            #we can round here
            compare = (grade // 10) * 10
            difference = grade - compare
            if difference > 2 and difference < 8:
                grade = compare + 5
            elif difference >= 8:
                grade = compare + 10
            print(grade)
        else:
            #we cant round here
            print(grade)

if __name__ == '__main__':
    grades = [0,84,99,38,37,80]
    gradingStudents(grades)
