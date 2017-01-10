#!/usr/bin/env python3
# @author slandau3

import unittest

from closers import valid_closers

class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(valid_closers('{{{{{{{{{adfkjaefia}}}}}}}'), False)

    def test2(self):
        self.assertEqual(valid_closers('{{{{{{{{{[[[[[[kadfa{{{{{{{((({daljfdaf({{{[]}}kaldjfs})})))}}}}}}}]]]]]]}kjfela}}}}}}}}'), True)

    def test3(self):
        self.assertEqual(valid_closers('{{{[}}}}dafda'), False)

    def test4(self):
        self.assertEqual(valid_closers('{{{{{{{{{}}}}}}}}}'), True)

    def test5(self):
        self.assertEqual(valid_closers('[[[[[[[[[kafjalfeianfailfeja;fjai;efa;sfj]]]]]]]]]kjajdain'), True)

    def test6(self):
        self.assertEqual(valid_closers(''), True)

    def test7(self):
        self.assertEqual(valid_closers('((((((fjdalfeja((((alefjalisj(())))))))))))d'), True)

    def test8(self):
        self.assertEqual(valid_closers(')))(((d'), False)


def quickie(): # quick function I wrote to generate correct strings
    a = input()
    output = ""
    for char in a:
        if char == '{':
            output = '}' + output
        elif char == '(':
            output = ')' + output
        elif char == '[':
            output = ']' + output

    print(a + output)


if __name__ == '__main__':
    unittest.main()