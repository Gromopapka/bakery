def c_fib(n):
    
    f1 = f2 = 1
    
    if n < 2:
        return 1

    for i in range(2, n):
        f1, f2 = f2, f1 + f2
    return(f2)