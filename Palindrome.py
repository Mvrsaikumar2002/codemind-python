n=int(input())
s=0
z=n
while n:
    r=n%10
    s=(s*10)+r
    n=n//10
if z==s:
    print("True")
else :
    print("False")