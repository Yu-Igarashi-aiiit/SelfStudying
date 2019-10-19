#c
n = int(input())
h = list(map(int,input().split()))
maxc=0
rec=n-1
for i in range(n-1,0,-1):
    if(i >rec):
        continue

    j = i
    cnt =0
    while((h[j]<=h[j-1])):
        if(j ==0):
            break
        cnt +=1
        j -=1
    rec= j
    if maxc < cnt:
        maxc = cnt
print(maxc)

#d
n = int(input())
print(n*(n-1)//2)
