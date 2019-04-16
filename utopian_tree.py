
def utopianTree(n):
    result = 1
    for x in range(1,n+1):
        if x % 2 != 0:
            result=result*2
        else:
            result+=1

    return result

if __name__ == '__main__':
    n = 5
    print(utopianTree(n))
