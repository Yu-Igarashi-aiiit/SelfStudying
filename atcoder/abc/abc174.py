# # # # # import sys
# # # # # from io import StringIO
# # # # # import unittest


# # # # # class TestClass(unittest.TestCase):
# # # # #     def assertIO(self, input, output):
# # # # #         stdout, stdin = sys.stdout, sys.stdin
# # # # #         sys.stdout, sys.stdin = StringIO(), StringIO(input)
# # # # #         resolve()
# # # # #         sys.stdout.seek(0)
# # # # #         out = sys.stdout.read()[:-1]
# # # # #         sys.stdout, sys.stdin = stdout, stdin
# # # # #         self.assertEqual(out, output)

# # # # #     def test_入力例_1(self):
# # # # #         input = """25"""
# # # # #         output = """No"""
# # # # #         self.assertIO(input, output)

# # # # #     def test_入力例_2(self):
# # # # #         input = """30"""
# # # # #         output = """Yes"""
# # # # #         self.assertIO(input, output)

# # # # # def resolve():
# # # # # x= int(input())
# # # # # if(x>=30):
# # # # #     print("Yes")
# # # # # else:
# # # # #     print("No")


# # # # # if __name__ == "__main__":
# # # # #     unittest.main()




# # # # #b
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
# # # #         input = """4 5
# # # # 0 5
# # # # -2 4
# # # # 3 4
# # # # 4 -4"""
# # # #         output = """3"""
# # # #         self.assertIO(input, output)

# # # #     def test_入力例_2(self):
# # # #         input = """12 3
# # # # 1 1
# # # # 1 1
# # # # 1 1
# # # # 1 1
# # # # 1 2
# # # # 1 3
# # # # 2 1
# # # # 2 2
# # # # 2 3
# # # # 3 1
# # # # 3 2
# # # # 3 3"""
# # # #         output = """7"""
# # # #         self.assertIO(input, output)

# # # #     def test_入力例_3(self):
# # # #         input = """20 100000
# # # # 14309 -32939
# # # # -56855 100340
# # # # 151364 25430
# # # # 103789 -113141
# # # # 147404 -136977
# # # # -37006 -30929
# # # # 188810 -49557
# # # # 13419 70401
# # # # -88280 165170
# # # # -196399 137941
# # # # -176527 -61904
# # # # 46659 115261
# # # # -153551 114185
# # # # 98784 -6820
# # # # 94111 -86268
# # # # -30401 61477
# # # # -55056 7872
# # # # 5901 -163796
# # # # 138819 -185986
# # # # -69848 -96669"""
# # # #         output = """6"""
# # # #         self.assertIO(input, output)

# # # # def resolve():
# # # #     n,d=map(int,input().split())
# # # #     x =[0]*n
# # # #     y=[0]*n

# # # #     import math

# # # #     for i in range(n):
# # # #         x[i],y[i]=map(int,input().split())

# # # #     cnt=0
# # # #     for elem in zip(x,y):
# # # #         if (math.sqrt(elem[0]**2+elem[1]**2) <=d):
# # # #             cnt+=1

# # # #     print(cnt)

# # # # if __name__ == "__main__":
# # # #     unittest.main()


# # # #c
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
# # #         input = """101"""
# # #         output = """4"""
# # #         self.assertIO(input, output)

# # #     def test_入力例_2(self):
# # #         input = """2"""
# # #         output = """-1"""
# # #         self.assertIO(input, output)

# # #     def test_入力例_3(self):
# # #         input = """999983"""
# # #         output = """999982"""
# # #         self.assertIO(input, output)


# # # def resolve():
# # #     k=int(input())



# # # if __name__ == "__main__":
# # #     unittest.main()





# # #d
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
# #         input = """4
# # WWRR"""
# #         output = """2"""
# #         self.assertIO(input, output)

# #     def test_入力例_2(self):
# #         input = """2
# # RR"""
# #         output = """0"""
# #         self.assertIO(input, output)

# #     def test_入力例_3(self):
# #         input = """8
# # WRWWRWRR"""
# #         output = """3"""
# #         self.assertIO(input, output)

# # def resolve():
# # n=int(input())
# # c=input()

# # from collections import Counter
# # cl = list(c)
# # cun= Counter(cl)
# # cn=cun["R"]
# # cnt=0
# # for i in  range(cn):
# #     if c[i]=="W" :
# #         rpos=c.rfind("R",cn)
# #         cl[i],cl[rpos]=cl[rpos],cl[i]
# #         cnt+=1

# # print(cnt)


# # if __name__ == "__main__":
# #     unittest.main()



# #f

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
#         input = """4 3
# 1 2 1 3
# 1 3
# 2 4
# 3 3"""
#         output = """2
# 3
# 1"""
#         self.assertIO(input, output)

#     def test_入力例_2(self):
#         input = """10 10
# 2 5 6 5 2 1 7 9 7 2
# 5 5
# 2 4
# 6 7
# 2 2
# 7 8
# 7 9
# 1 8
# 6 9
# 8 10
# 6 8"""
#         output = """1
# 2
# 2
# 1
# 2
# 2
# 6
# 3
# 3
# 3"""
#         self.assertIO(input, output)

# def resolve():
#     n,q=map(int,input().split())
#     c =list(map(int,input().split()))
#     l=[0]*q
#     r=[0]*q
#     for i in range(q):
#         l[i],r[i]=map(int,input().split())

#     for elem in zip(l,r):
#         print(len(set(c[elem[0]-1:elem[1]])))

# if __name__ == "__main__":
#     unittest.main()



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
        input = """101"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999983"""
        output = """999982"""
        self.assertIO(input, output)


def resolve():
    k=int(input())

    for i in range(20):
        st="7" * i
        a=int(st)
        if a%k==0:
            print(k)
            return
    
    print(-1)


if __name__ == "__main__":
    unittest.main()
