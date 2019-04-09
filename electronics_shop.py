import os
import sys

def getMoneySpent(b,m,n):
    max = -1

    for keyboard in m:
        for usb in n:
            total = keyboard + usb
            if (total >= max) and (total <= b):
                max = total
    return max

if __name__ == '__main__':
    b = 60
    m = [40,50,60]
    n = [5,8,12]

    print(getMoneySpent(b,m,n))
