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
#         input = """4 5"""
#         output = """unsafe"""
#         self.assertIO(input, output)
#     def test_入力例_2(self):
#         input = """100 2"""
#         output = """safe"""
#         self.assertIO(input, output)
#     def test_入力例_3(self):
#         input = """10 10"""
#         output = """unsafe"""
#         self.assertIO(input, output)

# def resolve():
# s,w = map(int,input().split())
# if(s<=w):
#     print("unsafe")
# else:
#     print("safe")

# if __name__ == "__main__":
#     unittest.main()

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
#         input = """10 9 10 10"""
#         output = """No"""
#         self.assertIO(input, output)
#     def test_入力例_2(self):
#         input = """46 4 40 5"""
#         output = """Yes"""
#         self.assertIO(input, output)

# def resolve():
# a,b,c,d  = map(int,input().split())
# for i in range(1,1000):
#     if(i%2!=0):
#         c -= b
#     else:
#         a -= d
    
#     if(a<=0):
#         print("No")
#         break
#     elif(c<=0):
#         print("Yes")
#         break

# if __name__ == "__main__":
#     unittest.main()

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
# apple
# orange
# apple"""
#         output = """2"""
#         self.assertIO(input, output)
#     def test_入力例_2(self):
#         input = """5
# grape
# grape
# grape
# grape
# grape"""
#         output = """1"""
#         self.assertIO(input, output)
#     def test_入力例_3(self):
#         input = """4
# aaaa
# a
# aaa
# aa"""
#         output = """4"""
#         self.assertIO(input, output)


# def resolve():
# n = int(input())
# s = [input() for _ in range(n)]

# print(len(set(s)))

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
        input = """1817181712114"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """14282668646"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2119"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
    s  = input()[::-1] #このスライスで逆順になるらしい

    #各桁を１０進数の桁とみなしたmodの計算
    a= [s[i] % pow(10,i) for i in range(len(s))]

    




if __name__ == "__main__":
    unittest.main()