def fib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:  
        return fib(n-1) + fib(n-2)
def test_fib():
    assert fib(6)==13
    assert fib(5)==8
    print ("Nice dude")

test_fib()