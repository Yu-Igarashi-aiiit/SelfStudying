#a
x,b = map(int,input().split())
if x<b:
    print("0")
else : print("10")

#b
n,x = map(int,input().split())
l = list(map(int,input().split()))
d = [0]*(n+1)
cnt =  0
for i in range(len(d)):
    if(i==0):
        d[i] = 0
    else :
        d[i] = d[i-1] + l[i-1]
    if(d[i]>x):
        break
    cnt += 1
print(cnt)
