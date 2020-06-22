# #a
# import sys
# from io import StringIO
# import unittest

# class TestClass(unittest.TestCase):
#     def assertIO(self, input, output):
#         stdout, stdin = sys.stdout, sys.stdin
#         sys.stdout, sys.stdin = StringIO(), StringIO(input)
#         resolve()
#         sys.stdout.seek(0)
#         out = sys.stdout.read()[:-1]
#         sys.stdout, sys.stdin = stdout, stdin
#         self.assertEqual(out, output)
#     def test_入力例_1(self):
#         input = """1 2 3"""
#         output = """3 1 2"""
#         self.assertIO(input, output)
#     def test_入力例_2(self):
#         input = """100 100 100"""
#         output = """100 100 100"""
#         self.assertIO(input, output)
#     def test_入力例_3(self):
#         input = """41 59 31"""
#         output = """31 41 59"""
#         self.assertIO(input, output)


# def resolve():
#     x,y,z = map(int,input().split())
#     print(z,x,y)

# if __name__ == "__main__":
#     unittest.main()


# import sys
# from io import StringIO
# import unittest
# import heapq

# class TestClass(unittest.TestCase):
#     def assertIO(self, input, output):
#         stdout, stdin = sys.stdout, sys.stdin
#         sys.stdout, sys.stdin = StringIO(), StringIO(input)
#         resolve()
#         sys.stdout.seek(0)
#         out = sys.stdout.read()[:-1]
#         sys.stdout, sys.stdin = stdout, stdin
#         self.assertEqual(out, output)
#     def test_入力例_1(self):
#         input = """4 1
# 5 4 2 1"""
#         output = """Yes"""
#         self.assertIO(input, output)
#     def test_入力例_2(self):
#         input = """3 2
# 380 19 1"""
#         output = """No"""
#         self.assertIO(input, output)
#     def test_入力例_3(self):
#         input = """12 3
# 4 56 78 901 2 345 67 890 123 45 6 789"""
#         output = """Yes"""
#         self.assertIO(input, output)

# def resolve():
#     n,m = map(int,input().split())
#     a = list(map(int,input().split()))
#     all =  sum(a)
    
    
#     a1 = list(map(lambda x: x*(-1), a))  # 各要素を-1倍
#     heapq.heapify(a1)
    
#     flg=0
#     for i in range(m):
#         tmp = -1*(heapq.heappop(a1))
#         if(tmp*m*4 >= all):
#             continue
#         else:
#             flg=1
#             break
#     if(flg==0):
#         print("Yes")
#     else:
#         print("No")

# if __name__ == "__main__":
#     unittest.main()


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
        input = """7 4"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 6"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1000000000000000000 1"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
    n,k = map(int,input().split())
    
    if(n%k==0):
        print("0")
    elif(n>k):
        ans1 = n % k
        ans2 = abs(ans1-k)
    
        if(abs(ans1)<abs(ans2)):
            print(ans1)
        else:
            print(ans2)
    else:
        ans = abs(n-k)
        if(ans<n):
            print(ans)
        else:
            print(n)

if __name__ == "__main__":
    unittest.main()