# # # # import sys
# # # # from io import StringIO
# # # # import unittest


# # # # class TestClass(unittest.TestCase):
# # # #     def assertIO(self, input, output):
# # # #         stdout, stdin = sys.stdout, sys.stdin
# # # #         sys.stdout, sys.stdin = StringIO(), StringIO(input)
# # # #         resolve()
# # # #         sys.stdout.seek(0)
# # # #         out = sys.stdout.read()[:-1]
# # # #         sys.stdout, sys.stdin = stdout, stdin
# # # #         self.assertEqual(out, output)

# # # #     def test_入力例_1(self):
# # # #         input = """B"""
# # # #         output = """A"""
# # # #         self.assertIO(input, output)

# # # #     def test_入力例_2(self):
# # # #         input = """a"""
# # # #         output = """a"""
# # # #         self.assertIO(input, output)

# # # # def resolve():
# # # # a =  input()
# # # # if(str.isupper(a)):
# # # #     print("A")
# # # # else : 
# # # #     print("a")

# # # # if __name__ == "__main__":
# # # #     unittest.main()

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
# # #         input = """5 3
# # # 50 100 80 120 80"""
# # #         output = """210"""
# # #         self.assertIO(input, output)

# # #     def test_入力例_2(self):
# # #         input = """1 1
# # # 1000"""
# # #         output = """1000"""
# # #         self.assertIO(input, output)


# # # def resolve():
# # # n,k = map(int,input().split())
# # # p = list(map(int,input().split()))

# # # p.sort()

# # # m = 0
# # # for i in range(k):
# # #     m += p[i]

# # # print(m)
    


# # # if __name__ == "__main__":
# # #     unittest.main()

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
# #         input = """2"""
# #         output = """b"""
# #         self.assertIO(input, output)

# #     def test_入力例_2(self):
# #         input = """27"""
# #         output = """aa"""
# #         self.assertIO(input, output)

# #     def test_入力例_3(self):
# #         input = """123456789"""
# #         output = """jjddja"""
# #         self.assertIO(input, output)

# # def resolve():
# #     n = int(input())



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
#         input = """4
# 1 2 3 4
# 3
# 1 2
# 3 4
# 2 4"""
#         output = """11
# 12
# 16"""
#         self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """4
# 1 1 1 1
# 3
# 1 2
# 2 1
# 3 5"""
#         output = """8
# 4
# 4"""
#         self.assertIO(input, output)

#     def test_入力例_3(self):
#         input = """2
# 1 2
# 3
# 1 100
# 2 100
# 100 1000"""
#         output = """102
# 200
# 2000"""
#         self.assertIO(input, output)


# def resolve():
# n = int(input())
# a = list(map(int,input().split()))
# q = int(input())
# b= [0]*q
# c= [0]*q
# for i in range(q):
#     b[i],c[i] = map(int,input().split())

# import collections
# co = collections.Counter(a)

# ans = sum(a)

# for i in range(q):
#     co[c[i]] += co[b[i]]
#     ans = ans + (c[i]-b[i])*co[b[i]]
#     co[b[i]] = 0
#     print(ans)


# if __name__ == "__main__":
#     unittest.main()
