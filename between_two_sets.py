def getTotalX(list1,list2):

    minimum = max(list1)
    maximum = min(list2)

    result = 0

    for x in range(minimum,maximum + 1):
        flag = True
        for number in list1:
            if x % number != 0:
                flag = False
        for number in list2:
            if number % x != 0:
                flag = False

        if flag == True:
            result+=1

    print(result)

if __name__ == '__main__':

    list1 = [2,6]
    list2 = [24,36]

    getTotalX(list1,list2)
