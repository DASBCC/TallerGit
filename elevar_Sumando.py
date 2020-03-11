def ES(x,y):
    if y==1:
        return x
    else:
        return x+ES(x,y-1)
print (ES(3,5))