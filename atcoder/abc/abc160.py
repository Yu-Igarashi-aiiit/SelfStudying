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
        input = """20 3
5 10 15"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """20 3
0 5 15"""
        output = """10"""
        self.assertIO(input, output)

def resolve():

    k,n = map(int,input().split())
    a= list(map(int,input().split()))

    ma=0
    for i in range(n-1,-1,-1):
        




if __name__ == "__main__":
    unittest.main()