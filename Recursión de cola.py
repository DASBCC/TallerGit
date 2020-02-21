def cd_cola (n):
    return cd_aux (n,1)

def cd_aux (n, contador):
    if n<10:
        return contador
    else: 
        return cd_aux (n//10, contador+1)
print(cd_cola(12))