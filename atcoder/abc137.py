#A - +-x

a,b = map(int,input().split())
print(max((a+b),(a-b),(a*b)))


#B - One Clue

k,x = map(int,input().split())
li =  []
for i in range(k):
    if i == 0:
        li.append(x)
    else:
        li.append(x+i)
        li.append(x-i)

li.sort()
print(*li)
