s = input()
k = int(input())

cnt=0
tmp=[]
flg=0

for i in range(len(s)-1):
    if s[0]==s[-1] and s[-1]!=s[-2] and (k>=2):
        flg=1

    if s[i] == s[i+1]:
        tmp.append(s[i])
    elif(len(tmp) >= 1):
        cnt += len(tmp)+1
        tmp =[]

    if(i == len(s)-2):
        if(len(tmp) >= 1):
            cnt += len(tmp)+1
            tmp =[]

if(flg==1):
    print((cnt//2+1)*k-1)
else:
    print(cnt//2*k)
