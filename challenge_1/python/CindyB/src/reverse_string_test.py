import unittest

from reverse_string import reverseString

class TestReverseString(unittest.TestCase):

    def test_zeroLengthInput(self):
        """We expect an empty string to be returned"""
        self.assertEqual(reverseString(None),None)

    def test_positiveLengthInput(self):
        """We expect the reverse string to be returned"""
        self.assertEqual(reverseString("hello"),"olleh")

if __name__ == '__main__':
    unittest.main()
