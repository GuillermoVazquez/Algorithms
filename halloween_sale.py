
def howManyGames(p, d, m, s):
    count = 0

    while(s >= p):
        s = s - p
        if p - d <= m:
            p = m
        else:
            p = p - d
        count+=1
    return count

if __name__ == '__main__':
    p = 16
    d = 2
    m = 1
    s = 9981
    print(howManyGames(p,d,m,s))
