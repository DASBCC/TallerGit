def CD(x):
    if 10>x:
        return 1
    else:
        return 1+CD(x//10)
def SC(x):
    if x<10:
        if x==0:
            return 1
        else:
            return x+x
    else:
        if x>=10:
            return (x//10**(CD(x)-1)+(x%10))*SC((x%10**(CD(x)-1))//10)
        
print (SC(324653))

