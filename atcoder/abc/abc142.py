#c
n = int(input())
a = list(map(int,input().split()))

dic = [0]*n
for i in range(n):
    dic[a[i]-1] = str(i+1)
print(" ".join(dic))

#d
import fractions
import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

a,b = map(int,input().split())
c = fractions.gcd(a,b)
lis = make_divisors(c)
cnt=0
for i in lis:
    if(is_prime(i)):
        cnt+=1
print(cnt+1)
