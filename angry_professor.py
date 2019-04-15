
def angryProfessor(k, a):
    #k = threshold
    #a = array
    count=0
    for time in a:
        if int(time) <= 0:
            count+=1
    print(count)
    if count >= k:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    k = 1
    a = "88 -17 -96 43 83 99 25 90 -39 86".split(" ")
    print(angryProfessor(k, a))
