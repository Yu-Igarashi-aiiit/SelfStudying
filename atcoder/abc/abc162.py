# # # import sys
# # # from io import StringIO
# # # import unittest

# # # class TestClass(unittest.TestCase):
# # #     def assertIO(self, input, output):
# # #         stdout, stdin = sys.stdout, sys.stdin
# # #         sys.stdout, sys.stdin = StringIO(), StringIO(input)
# # #         resolve()
# # #         sys.stdout.seek(0)
# # #         out = sys.stdout.read()[:-1]
# # #         sys.stdout, sys.stdin = stdout, stdin
# # #         self.assertEqual(out, output)
# # #     def test_入力例_1(self):
# # #         input = """117"""
# # #         output = """Yes"""
# # #         self.assertIO(input, output)
# # #     def test_入力例_2(self):
# # #         input = """123"""
# # #         output = """No"""
# # #         self.assertIO(input, output)
# # #     def test_入力例_3(self):
# # #         input = """777"""
# # #         output = """Yes"""
# # #         self.assertIO(input, output)

# # # def resolve():
# # # n=input()
# # # if("7" in set(n)):
# # #     print("Yes")
# # # else:
# # #     print("No")

# # # if __name__ == "__main__":
# # #     unittest.main()

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
#         input = """15"""
#         output = """60"""
#         self.assertIO(input, output)
#     def test_入力例_2(self):
#         input = """1000000"""
#         output = """266666333332"""
#         self.assertIO(input, output)

# def make_divisors(n):
#     divisors = []
#     for i in range(1, int(n**0.5)+1):
#         if n % i == 0:
#             divisors.append(i)
#             if i != n // i:
#                 divisors.append(n//i)

#     # divisors.sort()
#     return divisors


# def resolve():
# n = int(input())
# cnt=0
# for i in range(1,n+1):
#     if(i%3==0 or i%5==0):
#         continue
#     else:
#         cnt+=i

# print(cnt)

# if __name__ == "__main__":
#     unittest.main()

#c
import sys
from io import StringIO
import unittest


import math
from functools import reduce
# itertoolsモジュールからcombinations()をインポート
from itertools import combinations

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
        input = """2"""
        output = """9"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """200"""
        output = """10813692"""
        self.assertIO(input, output)


def resolve():
import math

n = int(input())
cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        t = math.gcd(i,j)
        for k in range(1,n+1):
            cnt +=  math.gcd(k,t)

print(cnt)


if __name__ == "__main__":
    unittest.main()