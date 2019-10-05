#a
s =  input()
li = ["Sunny","Cloudy","Rainy"]

if(s==li[0]):
    print(li[1])
elif(s==li[1]):
    print(li[2])
elif(s==li[2]):
    print(li[0])

#b
s = list(input())
flg=0
for i in range(1,len(s)+1):
    if(i%2!=0):
        if s[i-1] not in ["R","U","D"]:
            flg=1
    elif(i%2==0):
        if s[i-1] not in ["L","U","D"]:
            flg=1
if(flg==1):
    print("No")
else: print("Yes")

#c
n,k,q = map(int,input().split())
a = [int(input()) for i in range(q)]

li = [k]*n
for i in a:
    li[i-1] +=1
ans = list(map(lambda x:x-q,li))

for i in ans:
    if(i>=1):
        print("Yes")
    else : print("No")

#d
import heapq
n,m = map(int,input().split())
a=  list(map(int,input().split()))
h = list(map(lambda x:-1*x,a))
heapq.heapify(h)
for i in range(m):
    heapq.heapreplace(h,-(-h[0]//2))
print(-1*sum(h))

# a=sorted(a,reverse=True)
# for i in range(m):
#     if(a[i+1]>=a[i]):
#         a[i+1] //= 2
#     elif()
#
# print(sum(a))
