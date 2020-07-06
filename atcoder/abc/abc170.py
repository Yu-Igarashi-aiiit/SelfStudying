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
#         input = """6 5
# 4 7 10 6 5"""
#         output = """8"""
#         self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """10 5
# 4 7 10 6 5"""
#         output = """9"""
#         self.assertIO(input, output)

#     def test_入力例_3(self):
#         input = """100 0"""
#         output = """100"""
#         self.assertIO(input, output)

# def resolve():
#     x,n  = map(int,input().split())
#     p = list(map(int,input().split()))


#     m = 100
#     ans=100

#     for i in  range(0,103):
#         if(i in p):
#             continue

#         elif(abs(i-x) < m):
#             m = abs(i-x)
#             ans = i

#     print(ans)


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
        input = """5
24 11 8 3 16"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 5 5 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
33 18 45 28 8 19 89 86 2 4"""
        output = """5"""
        self.assertIO(input, output)

def resolve():


if __name__ == "__main__":
    unittest.main()
