
def beautifulTriplets(d, arr):
    #def of a beautiful troplet
    # i < j < k
    #a[j] - a[i] = a[k] - a[j] = d
    result = 0
    for x in range(len(arr)):
        if arr[x] + d in arr and arr[x] + d * 2 in arr:
            result+=1
    return result

if __name__ == '__main__':

    d = 3
    arr =[1,2,4,5,7,8,10]

    print(beautifulTriplets(d,arr))
