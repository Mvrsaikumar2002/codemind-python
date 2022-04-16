n=int(input())
sum=0
z=n
x=n
count=0
while n:
    r=n%10
    n=n//10
    count+=1
while count!=0:
    r=z%10
    c=pow(r,count)
    sum=sum+c
    z=z//10
    count-=1
if sum==x:
    print("True")
else:
    print("False")