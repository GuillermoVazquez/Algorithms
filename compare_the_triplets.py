def compare(alice, bob):
    aliceScore = 0
    bobScore = 0

    if alice[0] > bob[0]:
        aliceScore+=1
    elif alice[0] != bob[0]:
        bobScore+=1
    if alice[1] > bob[1]:
        aliceScore+=1
    elif alice[1] != bob[1]:
        bobScore+=1
    if alice[2] > bob[2]:
        aliceScore+=1
    elif alice[2] != bob[2]:
        bobScore+=1

    return aliceScore, bobScore



if __name__ == '__main__':
    alice = [1,2,3]
    bob = [1,3,2]
    aliceCompare , bobCompare = compare(alice, bob)
    print(aliceCompare,bobCompare)
