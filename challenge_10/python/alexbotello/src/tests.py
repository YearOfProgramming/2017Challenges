import unittest

from closers import is_valid_closer

class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_valid_closer('{{{{{{{{{adfkjaefia}}}}}}}'), False)

    def test2(self):
        self.assertEqual(is_valid_closer('{{{{{{{{{[[[[[[kadfa{{{{{{{((({daljfdaf({{{[]}}kaldjfs})})))}}}}}}}]]]]]]}kjfela}}}}}}}}'), True)

    def test3(self):
        self.assertEqual(is_valid_closer('{{{[}}}}dafda'), False)

    def test4(self):
        self.assertEqual(is_valid_closer('{{{{{{{{{}}}}}}}}}'), True)

    def test5(self):
        self.assertEqual(is_valid_closer('[[[[[[[[[kafjalfeianfailfeja;fjai;efa;sfj]]]]]]]]]kjajdain'), True)

    def test6(self):
        self.assertEqual(is_valid_closer(''), True)

    def test7(self):
        self.assertEqual(is_valid_closer('((((((fjdalfeja((((alefjalisj(())))))))))))d'), True)

    def test8(self):
        self.assertEqual(is_valid_closer(')))(((d'), False)


if __name__ == '__main__':
    unittest.main()
