N=int(input())
a,b=0,1
c=a+b
while c<=N:
    a=b
    b=c
    c=a+b
    if c==N:
        print("True")
        break
    else:
        continue
if c>N:
    print("False")
    