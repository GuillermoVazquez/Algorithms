import math

def diagonalDifference(array):

    number = len(array)

    primaryDiagonal = 0
    secondaryDiagonal = 0

    first = 0
    second = 0
    while(first < number and second < number):
        primaryDiagonal+=array[first][second]
        first+=1
        second+=1
    first = 0
    second = number - 1
    while(first < number and second >= 0):
        secondaryDiagonal+=array[first][second]
        first+=1
        second-=1

    result = abs(primaryDiagonal - secondaryDiagonal)
    return result

if __name__ == '__main__':
    array =[ [11, 2, 4],[4 ,5, 6],[10, 8, -12]]

    print( diagonalDifference(array) )
