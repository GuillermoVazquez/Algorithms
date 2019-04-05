import os
import sys
import math

#returns the last rank
def readRank(file):

    line = file.readline()
    while( file.readline() ):
        line = file.readline()

    return line

#writes the new rank info of the user
def writeRankInfo(file,rank,newRank,good,bad):
    file.write("----------\n")
    fullGood = "+" + good
    fullBad = "-" + bad
    percentile = (int(newRank) / 1300000) * 100

    file.write(fullGood+"\n")
    print(fullGood)
    print(fullBad)
    print(str(percentile) + "%")
    print(newRank)
    file.write(fullBad+"\n")
    file.write(newRank+"\n")

#updates the users rank
def update(file):

    #get the users last rank
    rank = readRank(file)
    newRank = input("new rank: ")
    #find the difference
    difference = int(rank) - int(newRank)
    good = 0
    bad = 0

    if difference > 0:
        good = difference
    else:
        bad = abs(difference)

    writeRankInfo(file,rank,newRank,str(good),str(bad))


if __name__ == '__main__':

    #check if ranking file already exists
    if os.path.exists("rank.txt"):
        #append to file
        file = open("rank.txt","r+")
    else:
        #create and write to file
        file = open("rank.txt","x")

    update(file)
    file.close()
