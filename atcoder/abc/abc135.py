
# A harmony
a,b = map(int,input().split())
k =  (a** 2 - b**2) / (2*(a-b))

if k.is_integer():
    print(int(k))
else : print("IMPOSSIBLE")

# B - 0 or 1 Swap
n = int(input())
p = list(map(int,input().split()))
k = 0

for i in range(len(p)):
    if p[i]!=i+1:
        k+=1
if(k<=2):
    print("YES")
elif(k>=3):
    print("NO")
