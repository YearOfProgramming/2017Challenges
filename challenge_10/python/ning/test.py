import unittest
from challenge_10 import check_close

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
                check_close('{{{{{{{{{adfkjaefia}}}}}}}'),
                False
                )

    def test_2(self):
        self.assertEqual(
                check_close('{{{{{{{{{[[[[[[kadfa{{{{{{{((({daljfdaf({{{[]}}kaldjfs})})))}}}}}}}]]]]]]}kjfela}}}}}}}}'),
                True
                )

    def test_3(self):
        self.assertEqual(
                check_close('{{{[}}}}dafda'),
                False
                )

    def test_4(self):
        self.assertEqual(
                check_close('{{{{{{{{{}}}}}}}}}'),
                True
                )

    def test_5(self):
        self.assertEqual(
                check_close('[[[[[[[[[kafjalfeianfailfeja;fjai;efa;sfj]]]]]]]]]kjajdain'),
                True
                )

    def test_6(self):
        self.assertEqual(
                check_close('< blank >'),
                True
                )

    def test_7(self):
        self.assertEqual(
                check_close('((((((fjdalfeja((((alefjalisj(())))))))))))d'),
                True
                )

    def test_8(self):
        self.assertEqual(
                check_close(')))(((d'),
                False
                )
    
    def test_9(self):
        self.assertEqual(
                check_close('({)}'),
                False
                )

if __name__ == '__main__':
    unittest.main()
