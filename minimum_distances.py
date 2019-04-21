import sys

def minimumDistances(a):

    min = sys.maxsize

    for x in range(len(a)):
        for y in range(x+1,len(a)):
            if (a[x] == a[y]) and (abs(x - y) < min):
                min = abs(x - y)
    return min

if __name__ == '__main__':
    example = [7,1,3,4,1,7]
    print(minimumDistances(example))
