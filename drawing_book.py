
def pageCount(n,p):

    numberOfSections = n//2 + 1

    distanceFromStart = p//2
    distanceFromEnd = numberOfSections - ( p//2 + 1)

    print(numberOfSections)
    print(distanceFromStart)
    print(distanceFromEnd)

if __name__ == '__main__':
    n = 5
    p = 5
    pageCount(n,p)
