#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
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
        print('------------')
        print(out)
        print('------------')
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """2 3 3
2 2
1 1
1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3 4
3 3
3 1
1 1
1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5 10
2 5
4 3
2 3
5 5
2 2
5 4
5 3
5 1
3 5
1 4"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
