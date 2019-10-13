#a
r = int(input())
print(3 * r **2)

#B
n,d = map(int,input().split())
if(n%(2*d+1)==0):
    print(n//(2*d+1))
else: print(n//(2*d+1)+1)

#c
n=int(input())
a=[int(input()) for i in range(n)]
ma = max(a)
fut_max = a.index(ma)
for i in range(n):
    if(i!=fut_max):
        print(ma)
    else:
        a.pop(fut_max)
        print(max(a))
