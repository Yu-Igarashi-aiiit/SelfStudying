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
# # # #         input = """7
# # # # 500 600"""
# # # #         output = """OK"""
# # # #         self.assertIO(input, output)
# # # #     def test_入力例_2(self):
# # # #         input = """4
# # # # 5 7"""
# # # #         output = """NG"""
# # # #         self.assertIO(input, output)
# # # #     def test_入力例_3(self):
# # # #         input = """1
# # # # 11 11"""
# # # #         output = """OK"""
# # # #         self.assertIO(input, output)

# # # # def resolve():
# # # # k= int(input())
# # # # a,b = map(int,input().split())
# # # # flg=0
# # # # for i in range(a,b+1):
# # # #     if(i%k==0):
# # # #         print("OK")
# # # #         flg=1
# # # #         break

# # # # if(flg==0):
# # # #     print("NG")

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
# # #         input = """103"""
# # #         output = """3"""
# # #         self.assertIO(input, output)
# # #     def test_入力例_2(self):
# # #         input = """1000000000000000000"""
# # #         output = """3760"""
# # #         self.assertIO(input, output)
# # #     def test_入力例_3(self):
# # #         input = """1333333333"""
# # #         output = """1706"""
# # #         self.assertIO(input, output)

# # # def resolve():
# # # x= int(input())

# # # i=100
# # # cnt = 0
# # # while(x>i):
# # #     i = int(i*1.01)
# # #     cnt +=1

# # # print(cnt)


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
# #         input = """3 4 3
# # 1 3 3 100
# # 1 2 2 10
# # 2 3 2 10"""
# #         output = """110"""
# #         self.assertIO(input, output)
# #     def test_入力例_2(self):
# #         input = """4 6 10
# # 2 4 1 86568
# # 1 4 0 90629
# # 2 3 0 90310
# # 3 4 1 29211
# # 3 4 3 78537
# # 3 4 2 8580
# # 1 2 1 96263
# # 1 4 2 2156
# # 1 2 0 94325
# # 1 4 3 94328"""
# #         output = """357500"""
# #         self.assertIO(input, output)
# #     def test_入力例_3(self):
# #         input = """10 10 1
# # 1 10 9 1"""
# #         output = """1"""
# #         self.assertIO(input, output)



# # def resolve():
# # import itertools
# # n,m,q = map(int,input().split())

# # a=[0]*q 
# # b=[0]*q
# # c=[0]*q
# # d=[0]*q

# # for i in range(q):
# #     a[i],b[i],c[i],d[i] = map(int,input().split())

# # k=list(itertools.combinations_with_replacement(range(1,m+1), n))

# # ma = 0
# # for elm in k:
# #     cnt = 0
# #     for j in range(q):
# #         if (elm[b[j]-1] - elm[a[j]-1] ==c[j]):
# #             cnt += d[j]
# #     if ma != max(ma,cnt):
# #         ma = cnt    
# # print(ma)

    

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
#         input = """5 7 4"""
#         output = """2"""
#         self.assertIO(input, output)
#     def test_入力例_2(self):
#         input = """11 10 9"""
#         output = """9"""
#         self.assertIO(input, output)

# def resolve():
#     a,b,n =map(int,input().split())

#     if(n<b):
#         ans = int(a*n/b) - a * int(n/b)
#         print(ans)

#     elif(n>=b):
#         ans = int(a*(b-1)/b) - a * int((b-1)/b)
#         print(ans)
    
    

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
        input = """4 1"""
        output = """2 3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7 3"""
        output = """1 6
2 5
3 4"""
        self.assertIO(input, output)

def resolve():
    n,m = map(int,input().split())
    


if __name__ == "__main__":
    unittest.main()