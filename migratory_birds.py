def migratoryBirds(arr):
    hash = [0]*5
    max = 0
    index = 0

    for bird in arr:
        hash[bird-1] += 1
        if hash[bird-1] > max:
            max = hash[bird-1]
            index = bird - 1
    print(hash)
    print(index + 1)
    return index + 1

if __name__ == '__main__':

    arr = [1,1,2,2,3,3]

    migratoryBirds(arr)
