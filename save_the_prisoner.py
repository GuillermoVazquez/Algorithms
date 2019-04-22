
def saveThePrisoner(n, m, s):
    while(m - 1 > 0):
    #pass the sweets out
        if s == n:
            s = 1
        else:
            s+=1
        m-=1

    return s

if __name__ == '__main__':
    #number of prisoners
    n = 352926151
    #number of sweets
    m = 380324688
    #chair number to start passing out treats
    s = 94730870
    print(saveThePrisoner(n,m,s))
