#Challenge 6: return ranges from a sorted list of integers

def returnRanges(intList):
    ranges=[]
    startRange=None
    endRange=None

    if len(intList) > 1:
        for i, val in enumerate(intList):
            #if it's the last item in the list
            if i == len(intList) - 1:
                #ends a range, append to ranges
                if val - 1 == intList[i - 1]:
                    endRange=val
                    ranges.append('%s->%s' % (startRange, endRange))
                continue
            #only start a range when the iteration begins one
            if startRange is None and val + 1 == intList[i + 1]:
                startRange=val
                endRange=None
                continue
            #Finish range when one has been started and the next value doesn't equal current + 1
            if val + 1 != intList[i + 1] and startRange is not None:
                endRange=val
                ranges.append('%s->%s' % (startRange, endRange))
                startRange=None
                endRange=None
    return ranges


if __name__ == '__main__':
    import unittest

    class TestRanges(unittest.TestCase):
        def test1(self):
            """
            Tests a basic input that should only have 1 element in the list
            :return:
            """
            self.assertEqual(returnRanges([1, 2]), ['1->2'])

        def test2(self):
            """
            Tests a case in which the return value should contain no elements
            :return:
            """
            self.assertEqual(returnRanges([1]), [])

        def test3(self):
            self.assertEqual(returnRanges([1, 2, 3, 4, 5, 8, 9, 10]), ['1->5', '8->10'])

        def test4(self):
            self.assertEqual(returnRanges([5, 6, 7, 20, 21, 22, 25]), ['5->7', '20->22'])

        def test5(self):
            self.assertEqual(returnRanges([5, 6, 9, 10, 12, 13, 15, 16, 18, 19, 25, 30]),
                             ['5->6', '9->10', '12->13', '15->16', '18->19'])

        def test6(self):
            self.assertEqual(returnRanges([5, 6, 7, 10, 15, 18, 20, 21, 22]), ['5->7', '20->22'])

    unittest.main()