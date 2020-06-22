import sys
from io import StringIO
import unittest
from collections import deque

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
        input = """0011"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """11011010001011"""
        output = """12"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
    s=input()
    sd=deque(s)
    d=deque()
    while(len(sd)>0):
        crr = sd.popleft()
        if(len(d)<1):
            d.append(crr)
            continue
        if(len(d)>=1 and d[-1]!=crr):
            d.pop()
        else:
            d.append(crr)
    print(len(s)-len(d))







if __name__ == "__main__":
    unittest.main()