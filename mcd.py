def Factorial(n):
    if n==1:
        return 1
    if n>=0:
        return n * Factorial (n-1)
    else:
        return n * Factorial (-n-1)
print (Factorial(8))   
print (Factorial(4))
