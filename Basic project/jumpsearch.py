import math
def jumpSearch(arr, x, n):
    step = math.sqrt(n)
    prev = 0 
    while arr[int(min(step, n)-1)] < x:
        prev = step 
        step += math.sqrt(n)
        if prev >= n :
            return -1

    if prev == min(step, n ):
        return -1
    if arr[int(prev)] == x:
        return prev
    return -1

# drive code
arr = [ 12, 67, 78, 45, 88, 22, 99, 54, 123, 90 ]
x = 12
n = len(arr)
index = jumpSearch(arr, x, n)
print("number" , x, "is at index" ,"%.0f" % index)
