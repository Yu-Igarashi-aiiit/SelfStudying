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
# # #         input = """16"""
# # #         output = """pon"""
# # #         self.assertIO(input, output)
# # #     def test_入力例_2(self):
# # #         input = """2"""
# # #         output = """hon"""
# # #         self.assertIO(input, output)
# # #     def test_入力例_3(self):
# # #         input = """183"""
# # #         output = """bon"""
# # #         self.assertIO(input, output)

# # # def resolve():
# # # n= input()

# # # if(int(n[-1])==3):
# # #     print("bon")
# # # elif(int(n[-1])==0 or int(n[-1])==1 or int(n[-1])==6 or int(n[-1])==8):
# # #     print("pon")
# # # else:
# # #     print("hon")


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
#         input = """7
# nikoandsolstice"""
#         output = """nikoand..."""
#         self.assertIO(input, output)
#     def test_入力例_2(self):
#         input = """40
# ferelibenterhominesidquodvoluntcredunt"""
#         output = """ferelibenterhominesidquodvoluntcredunt"""
#         self.assertIO(input, output)

# def resolve():
#     k= int(input())
#     s= input()

#     if(len(s)<=k):
#         print(s)
#     else:
#         print(s[:k]+"...")

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
        input = """3 4 9 0"""
        output = """5.00000000000000000000"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 4 10 40"""
        output = """4.56425719433005567605"""
        self.assertIO(input, output)

def resolve():

    import math

    a,b,h,m = map(int,input().split())

    sh = h*30
    lg = m*6

    th = min(abs(sh-lg),360-abs(sh-lg))
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(th)))
    print(c)





if __name__ == "__main__":
    unittest.main()


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
#         input = """4 4
# 1 2
# 2 3
# 3 4
# 4 2"""
#         output = """Yes
# 1
# 2
# 2"""
#         self.assertIO(input, output)
#     def test_入力例_2(self):
#         input = """6 9
# 3 4
# 6 1
# 2 4
# 5 3
# 4 6
# 1 5
# 6 2
# 4 5
# 5 6"""
#         output = """Yes
# 6
# 5
# 5
# 1
# 1"""
#         self.assertIO(input, output)

# def resolve():
#     n,m = map(int,input().split())
#     a,b = [0]*m,[0]*m
    
#     l = [[0]*n]*m
#     for i in range(m):
#         a[i],b[i] = map(int,input().split())
#         l[a[i]][b[i]] = 1

#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             if(l[i-1][j-1] != 0):
#                 dfs()

    

# def dfs(a):
#     # 数列の長さが N に達したら打ち切り
#     if len(A) == N:
#         # 処理
#         return
#     for v in range(M):
#         A.append(v)
#         dfs(A)
#         A.pop()


        
        
if __name__ == "__main__":
    unittest.main()
