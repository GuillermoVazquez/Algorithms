
def pickingNumbers(numbers):
    array = [0] * 100
    for number in numbers:
        array[number]+=1

    down = 0
    up = down + 1
    max = 0
    while up < len(array):
        count = array[down] + array[up]
        if count > max:
            max = count
        down+=1
        up+=1

    return max

if __name__ == '__main__':

    numbers = [4,6,5,3,3,1]
    print(pickingNumbers(numbers))
