def birthdayCakeCandles(numbers):
    max = 0
    counter = 1
    for number in numbers:
        if number == max:
            counter+=1
        if number > max:
            max = number
            counter = 1

    print(max)
    print(counter)


if __name__ == '__main__':
    nums = [4,4,1,3]
    birthdayCakeCandles(nums)
