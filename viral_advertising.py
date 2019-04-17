
def viralAdvertising(n):
    shared = 5
    liked = 0
    likedTotal = 0
    for x in range(1,n+1):
        liked = shared // 2
        likedTotal+=liked
        shared = liked * 3

    return likedTotal

if __name__ == '__main__':
    example = 5
    print(viralAdvertising(example))
