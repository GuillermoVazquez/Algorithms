def countApplesAndOranges(house,appleOrangeLocal,numbApplesNumOrr,appleFall,orangeFall):
    houseLeft = house[0]
    houseRigt = house[1]

    appleLocal = appleOrangeLocal[0]
    orangeLocal = appleOrangeLocal[1]

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
    house = [7,11]
    appleOrangeLocal = [5,15]
    numbApplesNumOrr = [3,2]
    appleFall = [-2,2,1]
    orangeFall = [5,-6]
    countApplesAndOranges(house,appleOrangeLocal,numbApplesNumOrr,appleFall,orangeFall)
