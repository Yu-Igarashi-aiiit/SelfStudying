# # import sys
# # from io import StringIO
# # import unittest

# # class TestClass(unittest.TestCase):
# #     def assertIO(self, input, output):
# #         stdout, stdin = sys.stdout, sys.stdin
# #         sys.stdout, sys.stdin = StringIO(), StringIO(input)
# #         resolve()
# #         sys.stdout.seek(0)
# #         out = sys.stdout.read()[:-1]
# #         sys.stdout, sys.stdin = stdout, stdin
# #         self.assertEqual(out, output)
# #     def test_入力例_1(self):
# #         input = """1"""
# #         output = """6.28318530717958623200"""
# #         self.assertIO(input, output)
# #     def test_入力例_2(self):
# #         input = """73"""
# #         output = """458.67252742410977361942"""
# #         self.assertIO(input, output)

# # import math

# # def resolve():
# #     r=int(input())
# #     print(2*r*math.pi)

# # if __name__ == "__main__":
# #     unittest.main()


# # #b


# # import sys
# # from io import StringIO
# # import unittest

# # class TestClass(unittest.TestCase):
# #     def assertIO(self, input, output):
# #         stdout, stdin = sys.stdout, sys.stdin
# #         sys.stdout, sys.stdin = StringIO(), StringIO(input)
# #         resolve()
# #         sys.stdout.seek(0)
# #         out = sys.stdout.read()[:-1]
# #         sys.stdout, sys.stdin = stdout, stdin
# #         self.assertEqual(out, output)
# #     def test_入力例_1(self):
# #         input = """41 2
# # 5 6"""
# #         output = """30"""
# #         self.assertIO(input, output)
# #     def test_入力例_2(self):
# #         input = """10 2
# # 5 6"""
# #         output = """-1"""
# #         self.assertIO(input, output)
# #     def test_入力例_3(self):
# #         input = """11 2
# # 5 6"""
# #         output = """0"""
# #         self.assertIO(input, output)
# #     def test_入力例_4(self):
# #         input = """314 15
# # 9 26 5 35 8 9 79 3 23 8 46 2 6 43 3"""
# #         output = """9"""
# #         self.assertIO(input, output)

# # def resolve():
# # n,m = map(int,input().split())
# # a= list(map(int,input().split()))


# # for i in a:
# #     n-=i
# # if n>=0 :
# #     print(n)
# # elif n < 0:
# #     print(-1)

# # if __name__ == "__main__":
# #     unittest.main()

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
#         input = """5
# 1 1 2 2"""
#         output = """2
# 2
# 0
# 0
# 0"""
#         self.assertIO(input, output)
#     def test_入力例_2(self):
#         input = """10
# 1 1 1 1 1 1 1 1 1"""
#         output = """9
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0"""
#         self.assertIO(input, output)
#     def test_入力例_3(self):
#         input = """7
# 1 2 3 4 5 6"""
#         output = """1
# 1
# 1
# 1
# 1
# 1
# 0"""
#         self.assertIO(input, output)

# import collections

# def resolve():
# n = int(input())
# a= list(map(int,input().split()))

# c = collections.Counter(a)
# for i in range(1,n+1):
#     if c[i] != None:
#         print(c[i])
#     else:
#         print(0)



# if __name__ == "__main__":
#     unittest.main()

#d
n,k = map(int,input().split())
##n+1からk以上を集める計算
##