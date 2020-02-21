def cdp(n):
    if n<10:
        if (n%2)==0:
            return 1
        else:
            return 0
    else:
        if (n%2)==0:
            return 1+cdp(n//10)
        else:
            return cdp (n//10)
print (cdp(n))


