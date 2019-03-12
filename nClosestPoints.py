import math

# n-closest points
# ok so this problem is prettty straightforward

# you are given a tuple of values ( each value is a pair of values )
# each value w/in the tuple represents a point on a graph
# you have to give the n closest points to the reference point given
# this is also good python practice for me! Python ( fyi ) was my first language!!!... but I don't use it that often :/


#soo lets go!

#input: tuple/reference/n
    #uses findNClosest() as a helper function
#output: array of n-closest indexes
def findDistance(array,reference,n):
    #this function will find the distances of each value and return an array of the points int their appropriate indexs
    ourList = []

    #lets parse through this array
    for a in array:
        #now lets get the two points and get distance from reference
        distance = math.sqrt( ( a[0]-reference[0] )**2 + ( a[1]-reference[1] )**2 )
        #now lets put the distance into our returning array
        ourList.append(distance)

    #now lets call findNClosest
    return findNClosest(ourList,n)


#input: a list of distances
#ouput: the n-closest points
def findNClosest(distances,n):

    returnList = []
    #lets sort the distance array
    #using insertion sort
    for i in range(1,len(distances)):
        key = distances[i]
        j = i - 1
        while j >= 0 and key < distances[j]:
            distances[j+1] = distances[j]
            j-=1
        distances[j+1] = key

    returnList.append(distances[0]);
    returnList.append(distances[1]);
    returnList.append(distances[2]);


    return returnList


#driver
def main():
    # let's declare our example tuple
    tup = ([0, -2], [-1, 0], [3, 5], [-2, -3], [3, 2])
    # our reference will be [0,0] to make it simple. algorithm works with all reference points
    reference = [0, 0]
    # n number
    n = 2

    #ok ok ok... lets split this up into 2 simple steps
    #1 we find the distance of each value from the reference
    #2 we find the n-closest points

    print findDistance(tup,reference,n)






if __name__ == '__main__':
    main()
