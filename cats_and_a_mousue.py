
def catAndMouse(x,y,z):
    #x = Cat A
    #y = Cat B
    #z = Mouse C
    distanceA = abs(z - x)
    distanceB = abs(z - y)

    if(distanceA == distanceB):
        return "Mouse C"
    elif distanceA < distanceB:
        return "Cat A"
    else:
        return "Cat B"

if __name__ == '__main__':
    x = 1
    y = 3
    z = 2
    print(catAndMouse(x,y,z))
