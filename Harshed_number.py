n=int(input())
s=0
z=n
while n:
    
    
    r=n%10
    s=s+r
    n=n//10
    
if z%s==0:
    print("True")
        
else:
    print("False")