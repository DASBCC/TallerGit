def SD(n):
    if 10>n:
        return n
    else: 
        return SD((n%10) + SD(n//10))
print (SD(120))