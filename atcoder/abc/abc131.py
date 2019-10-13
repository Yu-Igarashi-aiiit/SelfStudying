#a
a= list(input())
flg=0
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        flg =1
        break
if(flg==1):
    print("Bad")
elif(flg==0):
    print("Good")


#b
n,l=map(int,input().split())
li =[]
for i in range(1,n+1):
    li.append(i+l-1)

lis = list(map(abs,li))
li.pop(lis.index(min(lis)))
print(sum(li))

#c
###dcg,lcmは自作すること。ライブラリを使うと通らない場合が結構ある###
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)
a,b,c,d = map(int,input().split())
li=[]
gc = lcm(c,d)
for i in [a-1,b]:
    bc = i//c
    bd = i//d
    cd = i//gc
    li.append(i-(bc+bd-cd))
print(int(li[1]-li[0]))
