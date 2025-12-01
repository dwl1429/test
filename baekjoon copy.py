import sys


for i in range(100):
    n=0
    i+=1
    N = i
    while (((n+1)*n)//2) < N:
        n+=1
    k = N-(((n)*n-1)//2)
    b = n+1-k
    
    n = 0
    while (((n+1)*n)//2) < N:
        n+=1
    n-=1
    k2 = N-(((n+1)*n)//2)
    b2 = n+2-k
    if k2 != k:
        print(k,k2)
