#hello
#ok so this problem is pretty simple
#you are given an array, you must change the list so that all duplicates are sent to the back of the list
#ex./
#[2,1,3,4,4,9]
#[2,1,3,4,9,4]
#the length of the "unique" list within the original list along with the edited list will be the output


#input:
#list of integers
#output:
#length of "unique" list
#edited list
def noDups(array):
    start = 0
    for i in range(1, len(array) ):
        if array[start] != array[i]:
            start = start + 1
            array[start] = array[i]
    start = start + 1
    return start, array


if __name__ == '__main__':
    #example input:
    array = [2,1,3,4,4,9]
    length , newArray = noDups(array)
    print (length)
    print (newArray)