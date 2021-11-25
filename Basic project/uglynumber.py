# finding ugly numbers
# no. which are divided by 2, 3, 5 are not ugly
def maxDivide(a, b):
    while a % b == 0:
        a = a / b
    return a

def isugly(no):
    no = maxDivide(no,2)
    no = maxDivide(no,3)
    no = maxDivide(no,5)
    return 1 if no == 1 else 0

def getNthUglyNo(n):
    i = 1
    count = 1
    while n > count:
        i += 1
        if isugly(i):
            count += 1
    return i 
  
# Driver code to test above functions 
no = getNthUglyNo(56) 
print("nth ugly no. is ", no) 