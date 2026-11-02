def factorial(n): 
    res=1
    for x in range (1,n+1):
        res*=x
    return res

anw=factorial(8)
print(anw)