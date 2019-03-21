def staircase(n):
    #right-alligned staircase
    for x in range(1,n+1):
        print((" " * (n - x) ), end='')
        print("#" * x)

if __name__ == '__main__':
    staircase(6)
