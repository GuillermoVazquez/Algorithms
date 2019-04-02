import math

def breakingRecords(scores):

    result = [0,0]
    max = scores[0]
    min = scores[0]

    for x in range(1,len(scores)):

        if scores[x] > max:
            result[0]+=1
            max = scores[x]
        if scores[x] < min:
            result[1]+=1
            min = scores[x]
    print(result)
    return result

if __name__ == '__main__':

    scores = [3,4,21,36,10,28,35,5,24,42]
    breakingRecords(scores)
