def birthday(s,d,m):

    #length must equal the month
    #length must be contiguous
    #summation must be equal to day
    top = m - 1
    bottom = 0
    count = 0

    while top < len(s):
        sum = 0
        for x in range(bottom,top + 1):
            sum+=s[x]
        if sum == d:
            count+=1
        top+=1
        bottom+=1

    print(count)
    return count



if __name__ == '__main__':

    s = [1,2,1,3,2]
    d = 3
    m = 2

    birthday(s,d,m)
