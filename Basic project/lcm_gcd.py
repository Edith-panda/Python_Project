# finding gcd(greatest common divisor) of two numbers
def gcd(a,b):
    if a==0: 
        return b
    return gcd( b % a, a)
def lcm(a,b):
    return(a/gcd(a,b)) * b

# drive code for testing
a = 10
b = 45
print(" gcd of ",a, "and",b, gcd(a,b))
print(" lcm of ",a, "and",b, lcm(a,b))

# extended gcd imp used in case when a, b is coprime
def gcdExtended(a,b):
    if a == 0:
        return 0,1,b
    return(b %b , a)
    



