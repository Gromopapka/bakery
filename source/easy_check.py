def c_fib(k):
    if k < 2:
        return 1
    f1 = f2 = 1
    for i in range(2, k):
        f1, f2 = f2, f1 + f2
    return(f2)
