#A

def renew(lis,i,j):
    if lis[i][j]== 1:
        lis[i][j] =0
    else lis[i][j] = 1
    return lis

h,w,a,b = map(int,input().split())
li=[[0*j for j in range(b)] for j in range(a)]

for i in range(a):
    for j in range(b):
        tmph = li[][j]
        tmpw=li[i][]
        if tmph.count(1)<=a|tmph.count(0)<=a:
            True
        if tmpw.count(1)<=b|tmpw.count(0)<=b:

        li = renew(li,i,j)



#B
n,k = map(int,input().split())
p = list(map(int,input().split()))




#C

#D
