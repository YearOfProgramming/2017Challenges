#!/usr/bin/env python3
# @author slandau3

import unittest

from matching_brackets import matching_brackets

class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(matching_brackets('{{{{{{{{{adfkjaefia}}}}}}}'), False)

    def test2(self):
        self.assertEqual(matching_brackets('{{{{{{{{{[[[[[[kadfa{{{{{{{((({daljfdaf({{{[]}}kaldjfs})})))}}}}}}}]]]]]]}kjfela}}}}}}}}'), True)

    def test3(self):
        self.assertEqual(matching_brackets('{{{[}}}}dafda'), False)

    def test4(self):
        self.assertEqual(matching_brackets('{{{{{{{{{}}}}}}}}}'), True)

    def test5(self):
        self.assertEqual(matching_brackets('[[[[[[[[[kafjalfeianfailfeja;fjai;efa;sfj]]]]]]]]]kjajdain'), True)

    def test6(self):
        self.assertEqual(matching_brackets(''), True)

    def test7(self):
        self.assertEqual(matching_brackets('((((((fjdalfeja((((alefjalisj(())))))))))))d'), True)

    def test8(self):
        self.assertEqual(matching_brackets(')))(((d'), False)


if __name__ == '__main__':
    unittest.main()