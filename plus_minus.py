def plusMinus(array):
    #calculate the ratio of pos. neg. and 0's in array
    pos = 0
    neg = 0
    zero = 0

    for number in array:
        if number < 0:
            neg+=1
        elif number == 0:
            zero+=1
        else:
            pos+=1

    print("%0.6f" %(pos/len(array)))
    print("%0.6f" %(neg/len(array)))
    print("%0.6f" %(zero/len(array)))

if __name__ == '__main__':
    array = [1,1,0,-1,-1]
    plusMinus(array)
