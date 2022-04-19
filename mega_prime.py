
def fun(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c
n=int(input())
c=fun(n)
if c==2:
    while n:
        r=n%10
        c=fun(r)
        if c==2:
            n=n//10
        else:
            break
    if c==2:
        print("Mega Prime")

    else:
        print("Not Mega Prime")

else:
    print("Not Mega Prime")
