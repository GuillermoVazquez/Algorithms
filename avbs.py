def avbs(length, array):
    sum = 0
    for number in array:
        sum+=number
    return sum

if __name__ == '__main__':
    length = 5
    array = [1000000001,1000000002,1000000003,1000000004,1000000005]
    sum = avbs(length,array)
    print(sum)
