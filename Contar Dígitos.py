def CD(n):
    if 10>n:
        return 1
    else:
        return 1+CD(n//10)
    
print (CD(52532423423332))



