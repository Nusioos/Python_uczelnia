def fibonacci(n): 
    if n<=0:
        return 0
    res1=1
    res2=1
    anw=0
    for x in range (1,n+1):
        anw=res1
        res3=res1+res2
        res1=res2
        res2=res3
    return anw

anw=fibonacci(8)
print(anw)