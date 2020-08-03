# # # #a

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
# # #         input = """2"""
# # #         output = """4"""
# # #         self.assertIO(input, output)

# # #     def test_入力例_2(self):
# # #         input = """100"""
# # #         output = """10000"""
# # #         self.assertIO(input, output)

# # # def resolve():
# # # r= int(input())
# # # print(r**2)

# # # if __name__ == "__main__":
# # #     unittest.main()

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
# #         input = """6
# # abcabc"""
# #         output = """Yes"""
# #         self.assertIO(input, output)

# #     def test_入力例_2(self):
# #         input = """6
# # abcadc"""
# #         output = """No"""
# #         self.assertIO(input, output)

# #     def test_入力例_3(self):
# #         input = """1
# # z"""
# #         output = """No"""
# #         self.assertIO(input, output)


# # def resolve():
# #     n= int(input())
# #     s= input()
# #     harf = int(len(s)/2)

# #     if(s[:harf] == s[harf:]):
# #         print("Yes")
# #     else:
# #         print("No")

# # if __name__ == "__main__":
# #     unittest.main()





# #c
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
#         input = """3
# 0 0
# 1 0
# 0 1"""
#         output = """2.2761423749"""
#         self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """2
# -879 981
# -866 890"""
#         output = """91.9238815543"""
#         self.assertIO(input, output)

#     def test_入力例_3(self):
#         input = """8
# -406 10
# 512 859
# 494 362
# -955 -475
# 128 553
# -986 -885
# 763 77
# 449 310"""
#         output = """7641.9817824387"""
#         self.assertIO(input, output)

# def resolve():
# n= int(input())
# x= [0]*n
# y= [0]*n
# for i in range(n):
#     x[i],y[i]=map(int,input().split())

#
# import itertools
# import  math
# lis = list(itertools.permutations(range(n),n))

# al=0
# for elem in lis:
#     [al := al + math.sqrt( (x[elem[i]]-x[elem[i+1]])**2 +  (y[elem[i]]-y[elem[i+1]])**2) for i in range(n-1)]

# print(al/len(lis))

# if __name__ == "__main__":
#     unittest.main()





#d


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
        input = """3 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999999 999999"""
        output = """151840682"""
        self.assertIO(input, output)


def resolve():

    x,y = map(int,input().split())

    

if __name__ == "__main__":
    unittest.main()
