def simpleArraySum(array):
    sum = 0
    for number in array:
        sum+=number

    return sum

if __name__ == '__main__':
    array = [1,2,3,4,10,11]
    print(simpleArraySum(array))
