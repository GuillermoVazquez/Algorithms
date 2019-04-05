def migratoryBirds(arr):
    hash = [0]*5
    max = 0
    index = 0

    for bird in arr:
        bird = int(bird)
        hash[bird-1] += 1
        #if hash[bird-1] > max:
        #    index = bird - 1
        #    max = hash[bird-1]
    for x in range(len(hash)):
        if hash[x] > max:
            max = hash[x]
            index = x + 1
            
    return index

if __name__ == '__main__':
    #arr = [1,2,3,3,3,4,4,4]

    file = open("input04.txt","r")
    line = file.readline()
    line = file.readline()
    arr = line.split(" ")

    migratoryBirds(arr)
