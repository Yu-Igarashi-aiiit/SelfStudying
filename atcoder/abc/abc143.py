a,b = map(int,input().split())
if(a<=2*b):
    print(0)
else:
    print(a-2*b)

#b
n = int(input())
d = list(map(int,input().split()))

cnt=0
for i in range(0,len(d)-1):
    for j in range(i+1,len(d)):
        cnt += d[i]*d[j]
print(cnt)

#c
n = int(input())
s = input()
cnt=1
for i in range(n-1):
    if(s[i]==s[i+1]):
        continue
    else:
        cnt+=1

print(cnt)

#d
from bisect import bisect_left

n = int(input())
l = list(map(int,input().split()))

l.sort()
count = 0
for i in range(n-2):
  for j in range(i+1,n-1):
    count+=bisect_left(l,l[j]+l[i])-j-1
print(count)
218 786 704 233 645 728 389
