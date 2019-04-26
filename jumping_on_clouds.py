
def jumpingOnClouds(c):

    count = 0
    step = 0
    while( step < len(c)):
        if step + 2 < len(c) and c[step + 2] != 1:
            step = step + 2
            count+=1
        else:
            step = step + 1
            count+=1

    return count - 1 

if __name__ == '__main__':

    example = [0,0,0,0,1,0]
    print(jumpingOnClouds(example))
