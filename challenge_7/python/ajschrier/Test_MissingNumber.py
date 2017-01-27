import MissingNumber
import unittest


class BuiltInTests(unittest.TestCase):
    """tests for builtInMethod"""

    def testMissing3(self):
        self.assertEqual(MissingNumber.
                         builtInMethod([0, 1, 2, 4]), 3)

    def testMissing2(self):
        self.assertEqual(MissingNumber.
                         builtInMethod([1, 3, 4, 0]), 2)

    def testNoMissingNumber(self):
        self.assertEqual(MissingNumber.
                         builtInMethod([1, 2, 3]), 0)

    def testLongerList(self):
        self.assertEqual(MissingNumber.
                         builtInMethod([0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11,
                                        12, 13, 14, 15, 16, 17, 18, 19,
                                        20, 21, 22, 23, 24]), 7)

    def testEvenLongerRandomList(self):
        self.assertEqual(MissingNumber.
                         builtInMethod([78, 53, 118, 99, 154, 5, 52, 184,
                                       73, 17, 92, 107, 34, 159, 101, 30,
                                       171, 95, 100, 54, 63, 169, 37, 45,
                                       174, 158, 57, 0, 89, 61, 71, 188,
                                       83, 18, 133, 149, 62, 151, 90, 3,
                                       141, 126, 165, 179, 103, 166, 68,
                                       177, 163, 190, 77, 55, 31, 187, 16,
                                       91, 47, 93, 146, 147, 74, 185, 135,
                                       102, 41, 125, 164, 12, 19, 168, 96,
                                       23, 86, 194, 9, 132, 104, 122, 24,
                                       144, 161, 117, 183, 196, 176, 155,
                                       108, 172, 120, 160, 182, 50, 75, 22,
                                       15, 49, 80, 127, 106, 20, 148, 139,
                                       38, 134, 67, 123, 56, 88, 40, 186,
                                       131, 76, 59, 21, 43, 4, 14, 115,
                                       162, 199, 48, 128, 81, 39, 11, 97,
                                       137, 153, 10, 65, 138, 114, 79, 6,
                                       195, 156, 180, 8, 28, 60, 192, 42,
                                       119, 64, 2, 200, 116, 129, 51, 178,
                                       191, 121, 82, 143, 26, 110, 33, 136,
                                       32, 175, 27, 150, 111, 105, 70, 157,
                                       44, 13, 46, 170, 58, 69, 198, 193,
                                       167, 25, 29, 181, 66, 72, 36, 87, 7,
                                       98, 130, 152, 94, 189, 1, 84, 109,
                                       113, 197, 145, 35, 124, 112, 173,
                                       140, 142]), 85)


class SumMethodTests(unittest.TestCase):
    """tests for sumMethod"""

    def testMissing3(self):
        self.assertEqual(MissingNumber.
                         sumMethod([0, 1, 2, 4]), 3)

    def testMissing2(self):
        self.assertEqual(MissingNumber.
                         sumMethod([1, 3, 4, 0]), 2)

    def testNoMissingNumber(self):
        self.assertEqual(MissingNumber.
                         sumMethod([1, 2, 3]), 0)

    def testLongerList(self):
        self.assertEqual(MissingNumber.
                         sumMethod([0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11,
                                    12, 13, 14, 15, 16, 17, 18, 19,
                                    20, 21, 22, 23, 24]), 7)

    def testEvenLongerRandomList(self):
        self.assertEqual(MissingNumber.
                         sumMethod([78, 53, 118, 99, 154, 5, 52, 184,
                                    73, 17, 92, 107, 34, 159, 101, 30,
                                    171, 95, 100, 54, 63, 169, 37, 45,
                                    174, 158, 57, 0, 89, 61, 71, 188,
                                    83, 18, 133, 149, 62, 151, 90, 3,
                                    141, 126, 165, 179, 103, 166, 68,
                                    177, 163, 190, 77, 55, 31, 187, 16,
                                    91, 47, 93, 146, 147, 74, 185, 135,
                                    102, 41, 125, 164, 12, 19, 168, 96,
                                    23, 86, 194, 9, 132, 104, 122, 24,
                                    144, 161, 117, 183, 196, 176, 155,
                                    108, 172, 120, 160, 182, 50, 75, 22,
                                    15, 49, 80, 127, 106, 20, 148, 139,
                                    38, 134, 67, 123, 56, 88, 40, 186,
                                    131, 76, 59, 21, 43, 4, 14, 115,
                                    162, 199, 48, 128, 81, 39, 11, 97,
                                    137, 153, 10, 65, 138, 114, 79, 6,
                                    195, 156, 180, 8, 28, 60, 192, 42,
                                    119, 64, 2, 200, 116, 129, 51, 178,
                                    191, 121, 82, 143, 26, 110, 33, 136,
                                    32, 175, 27, 150, 111, 105, 70, 157,
                                    44, 13, 46, 170, 58, 69, 198, 193,
                                    167, 25, 29, 181, 66, 72, 36, 87, 7,
                                    98, 130, 152, 94, 189, 1, 84, 109,
                                    113, 197, 145, 35, 124, 112, 173,
                                    140, 142]), 85)


if __name__ == '__main__':
    unittest.main()
