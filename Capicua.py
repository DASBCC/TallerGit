def CD(n):
    if 10>n:
        return 1
    else:
        return 1+CD(n//10)
def Inv(n):
    if n<10:
        return n
    else:
        return (n%10)*(10**(CD(n)-1)) + Inv(n//10)
def Cap(n):
    if Inv(n)==n:
        return "Esa es"
    else:
        return "Está mamando"











print(Cap(12344421))
