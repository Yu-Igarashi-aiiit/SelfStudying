
#D
# 　差分更新の問題
# ある組み合わせ全体を構成する式を最初に作ってしまって、
# その式から、該当する要素が構成するオペランド（４＋３＋２とかの式の数字部分）
# を引いて、そのパターンのときの正しいオペランドを加算する方法。
# なぜこの方法がよいかというと、その要素が影響するオペランド以外は
# 更新の対象とはならないため。
#また重要な公式としてnCr = n(n-1)/2

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
1 1 2 1 2"""
        output = """2
2
3
2
3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """0
0
0
0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5
3 3 3 3 3"""
        output = """6
6
6
6
6"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """8
1 2 1 4 2 1 4 1"""
        output = """5
7
5
7
7
5
7
5"""
        self.assertIO(input, output)

import collections 
import math

def resolve():
    n=int(input())
    a=list(map(int,input().split()))

    cnt=0
    c =collections.Counter(a) #要素の数

    #全体の式の導出
    #今回は要素ごとの組み合わせの数

    for i in c.values() :
        cnt += i*(i-1)//2

    #各要素の影響を排除して出力
    for i in a:
        print(cnt- c[i]*(c[i]-1)//2 + (c[i]-1)*(c[i]-2)//2)



if __name__ == "__main__":
    unittest.main()

