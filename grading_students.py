def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade > 37:
            #we can round here
            compare = (grade // 10) * 10
            print(compare)
            difference = grade - compare
            print(difference)
            if difference > 2 and difference < 6:
                grade = compare + 5
            elif difference >= 8:
                grade = compare + 10
            result.append(grade)
        else:
            #we cant round here
            result.append(grade)
    return result

if __name__ == '__main__':
    grades = [73,67,38,33]
    result = gradingStudents(grades)
    print(result)
