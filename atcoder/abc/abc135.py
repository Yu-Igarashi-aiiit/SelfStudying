
# # A harmony
# a,b = map(int,input().split())
# k =  (a** 2 - b**2) / (2*(a-b))

# if k.is_integer():
#     print(int(k))
# else : print("IMPOSSIBLE")

# # B - 0 or 1 Swap
# n = int(input())
# p = list(map(int,input().split()))
# k = 0

# for i in range(len(p)):
#     if p[i]!=i+1:
#         k+=1
# if(k<=2):
#     print("YES")
# elif(k>=3):
#     print("NO")

#c
import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """2
3 5 2
4 5"""
        output = """9"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
5 6 3 8
5 100 8"""
        output = """22"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2
100 1 1
1 100"""
        output = """3"""
        self.assertIO(input, output)


def resolve():
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

cnt = 0
res = 0 #余力
for i in range(n):

    ch = min(a[i],res)
    cnt += ch
    a[i] -= ch
    if b[i] > a[i]:
        cnt += a[i]
        res = b[i] - a[i]
    else:
        cnt += b[i]
        res = 0

cnt += min(a[n],res)

print(cnt)





    
        


if __name__ == "__main__":
    unittest.main()