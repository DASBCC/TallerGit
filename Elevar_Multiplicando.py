def EM(x,y):
    if y==1:
        return x
    else:
        if y>1:
            return x*EM(x,y-1)
print (EM(5,3))
