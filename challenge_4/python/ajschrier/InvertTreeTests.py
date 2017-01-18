from InvertTree import flipTree, Node
import unittest


class InvertTreeTests(unittest.TestCase):
    """docstring for InvertTreeTests"""
    def testFlipTreeGivenCase(self):
        testTree = Node(4,
                        Node(2,
                             Node(1),
                             Node(3)),
                        Node(7,
                             Node(6),
                             Node(9)))
        resultTree = Node(4,
                          Node(7,
                               Node(9),
                               Node(6)),
                          Node(2,
                               Node(3),
                               Node(1)))
        self.assertEqual(flipTree(testTree), resultTree)

    def testFlipTreeNone(self):
        self.assertEqual(flipTree(None), None)

    def testFlipTreeDepth1(self):
        testTree = Node(1)
        resultTree = Node(1)
        self.assertEqual(flipTree(testTree), resultTree)


if __name__ == '__main__':
    unittest.main()
