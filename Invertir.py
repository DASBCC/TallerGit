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
print (Inv(780234807523098752397023597532097235097235907532907532))