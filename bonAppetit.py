
def bonAppetit(bill, k, b):
    #b = amount anna was charged
    #bill = list of items
    #k = the index of the item anna did not eat

    shared = 0

    for x in range(len(bill)):
        if x != k:
            shared += bill[x]

    if b == shared / 2:
        print( "Bon Appetit" )
    else:
        print("%.0f" %(b - (shared / 2)) )

if __name__ == '__main__':

    bill = [3,10,2,9]
    k = 1
    b = 7
    bonAppetit(bill, k, b)
