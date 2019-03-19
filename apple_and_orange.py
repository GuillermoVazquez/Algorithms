def countApplesAndOranges(houseStart,houseEnd,a,b,appleFall,orangeFall):
    houseLeft = houseStart
    houseRigt = houseEnd

    appleLocal = a
    orangeLocal = b

    appleHits = 0
    orangeHits = 0

    for apple in appleFall:
        if apple > 0:
            fallLocal = apple + appleLocal
            if fallLocal >= houseLeft and fallLocal <= houseRigt:
                appleHits+=1

    for orange in orangeFall:
        if orange < 0:
            fallLocal = orangeLocal + orange
            if fallLocal <= houseRigt and fallLocal >= houseLeft:
                orangeHits+=1

    print(appleHits)
    print(orangeHits)


if __name__ == '__main__':
    houseStart = 7
    houseEnd = 11
    a = 5
    b = 15
    appleFall = [-2,2,1]
    orangeFall = [5,-6]
    countApplesAndOranges(houseStart,houseEnd,a,b,appleFall,orangeFall)
