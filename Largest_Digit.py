n=int(input())
c=0
s=0
while n>0:
    r=n%10
    if r>0 and s<r:
        s=r
    c=r
    
    n=n//10
print(s)