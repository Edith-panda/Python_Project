# linear search 
# finding the element in array
def search(arr,n, x):
    for i in range (0,n):
        if (arr[i] ==x):
            return i 
            return -1 
arr = [ 2, 3, 5, 80, 59, 34567, 34, 12 ]
x = 34567
n = len(arr)
result = search(arr,n, x)
if (result == -1):
    print(" this is not present in array ")
else:
    print(" this is present in array at index ", result)
# binary search 
# fing the element using binery search

def binarySearch (arr, l, r, x):

    if r >=1:
        mid = 1 + (r-1)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr , 1 , mid-1 , x)
        else :
            return binarySearch(arr , 1 , mid+1 , x)
    else :
        return -1

#drive code
arr = [ 12, 45, 67, 34, 23456, 34567, 89, 1, 2, 50, 78]
x = 1
result = binarySearch(arr, 0, len(arr) -1, x)
if result != -1:
    print(" this number is in array at index % d  " % result)
else:
    print("this number is not in array")
        


