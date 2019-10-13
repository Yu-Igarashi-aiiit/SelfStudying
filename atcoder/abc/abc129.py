#  a
p,q,r = map(int,input().split())
print(p+q+r-max(p,q,r))

 # b
n= int(input())
w = list(map(int,input().split()))

tmp =sum(w)

for i in range(n):
    bf=sum(w[:i])
    af=sum(w[i:])
    if(tmp > (abs(bf-af))):
        tmp = (abs(bf-af))

print(tmp)
