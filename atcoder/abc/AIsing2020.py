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
# # # #         input = """5 10 2"""
# # # #         output = """3"""
# # # #         self.assertIO(input, output)

# # # #     def test_入力例_2(self):
# # # #         input = """6 20 7"""
# # # #         output = """2"""
# # # #         self.assertIO(input, output)

# # # #     def test_入力例_3(self):
# # # #         input = """1 100 1"""
# # # #         output = """100"""
# # # #         self.assertIO(input, output)

# # # # def resolve():
# # # # l,r,d = map(int,input().split())
# # # # cnt=0
# # # # for i in range(l,r+1):
# # # #     if i%d == 0:
# # # #         cnt+=1
# # # # print(cnt)

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
# # #         input = """5
# # # 1 3 4 5 7"""
# # #         output = """2"""
# # #         self.assertIO(input, output)

# # #     def test_入力例_2(self):
# # #         input = """15
# # # 13 76 46 15 50 98 93 77 31 43 84 90 6 24 14"""
# # #         output = """3"""
# # #         self.assertIO(input, output)

# # # def resolve():
# # # n= int(input())
# # # a=list(map(int,input().split()))
# # # cnt=0
# # # for i in range(1,n+1,2):
# # #     if a[i-1]%2 != 0:
# # #         cnt+=1
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
# #         input = """20"""
# #         output = """0
# # 0
# # 0
# # 0
# # 0
# # 1
# # 0
# # 0
# # 0
# # 0
# # 3
# # 0
# # 0
# # 0
# # 0
# # 0
# # 3
# # 3
# # 0
# # 0"""
# #         self.assertIO(input, output)


# # # cnt = 0

# # def dfs(lis,cnt,n):
# #     if sum(lis)>100:
# #         return cnt

# #     if(len(lis)==3):
# #         ans=lis[0]**2+lis[1]**2+lis[2]**2+lis[0]*lis[1]+lis[1]*lis[2]+lis[2]*lis[0]
# #         if(ans==n):
# #             cnt+=1
# #         return cnt
    
# #     for v in range(1,100):
# #         lis.append(v)
# #         cnt=dfs(lis,cnt,n)
# #         lis.pop()
    
# #     return cnt

# # def resolve():
# # n= int(input())
# # for i in range(1,n+1):
# #     cnt = 0
# #     print(dfs([],cnt,i))

# # if __name__ == "__main__":
# #     unittest.main()




# #d

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
        input = """3
011"""
        output = """2
1
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """23
00110111001011011001110"""
        output = """2
1
2
2
1
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
1
3"""
        self.assertIO(input, output)


def resolve():
    n =int(input())
    xt = input()

    for i in range(n):
        x = xt
        if x[i]=="0":
            if(i==0):
                x = "1" + x[i+1:]
            else:
                x= x[:i] + "1" + x[i:]
        else:
            if(i==0):
                x = "0" + x[i+1:]
            else:
                x= x[:i] + "0" + x[i:]

        pop = x.count("1")
        num = "0b"+x
        print(pop,int(num,2))



if __name__ == "__main__":
    unittest.main()



