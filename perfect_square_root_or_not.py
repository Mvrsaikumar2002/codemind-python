n=int(input())
for i in range(1,n+1):
    p= i*i
    if n==p:
        print("True")
        break
    elif i>n//2:
        print("False")
        break
    