def fib_ans(N):
    a,b=0,1
    print(a,end=' ')
    print(b,end=' ')
    c=a+b
    
    for i in range(3,N):
        print(c,end=' ')
        a=b
        b=c
        c=a+b
    return c    
N=int(input())    
res=fib_ans(N)
print(res)