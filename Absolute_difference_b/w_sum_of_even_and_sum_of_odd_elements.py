n=int(input())
l=list(map(int,input().split()))
es=0
os=0
for i in l:
    if i%2==0:
        es=es+i
    else:
        os=os+i
k=abs(os-es)
print(k)