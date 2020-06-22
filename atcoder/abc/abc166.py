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
# #         input = """ABC"""
# #         output = """ARC"""
# #         self.assertIO(input, output)

# # def resolve():

# # s= input()
# # if(s=="ABC"):
# #     print("ARC")
# # elif(s=="ARC"):
# #     print("ABC")



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
#         input = """3 2
# 2
# 1 3
# 1
# 3"""
#         output = """1"""
#         self.assertIO(input, output)
#     def test_入力例_2(self):
#         input = """3 3
# 1
# 3
# 1
# 3
# 1
# 3"""
#         output = """2"""
#         self.assertIO(input, output)

# def resolve():
# n,k = map(int,input().split())
# a=[]
# for i in range(k):
#     d = int(input())
#     a.append(list(map(int,input().split())))

# ans = [i for i in range(1,n+1)]
# for i in a:
#     for j in i:
#         if j in ans:
#             ans.remove(j)

# print(len(ans))

    


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
        input = """4 3
1 2 3 4
1 3
2 3
2 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
    import collections

    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())

    z = zip(a,b)
    lis = [0]*n

    for i,j in z:

        if h[i-1] > h[j-1]:
            lis[j-1] = 1
        elif h[i-1] < h[j-1]:
            lis[i-1] = 1
        else:
            lis[i-1]=1
            lis[j-1]=1

    print(collections.Counter(lis)[0])
    

    

if __name__ == "__main__":
    unittest.main()