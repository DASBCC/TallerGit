def Factorial(n):
    if n==1:
        return 1
    if n>=0:
        return n * Factorial (n-1)
    else:
        return n * Factorial (-n-1)
def test_Factorial():
    assert Factorial(1)==1
    assert Factorial(3)==6
    print ("Pruebas exitosas")


test_Factorial()