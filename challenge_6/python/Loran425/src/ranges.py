__author__ = "Loran425"


def ranges(lst):
    temp_start = None
    temp_end = None
    prev = None
    output = []

    for x in lst:
        temp_end = x

        if temp_start is None:
            temp_start = x
            prev = x
            continue

        if temp_end != prev + 1:
            if temp_start != prev:  # single number isn't a range
                output.append('{}->{}'.format(temp_start, prev))
            temp_start = x
            prev = x
            continue
        else:
            prev = x

    # Make sure the final range makes it into the output
    if temp_start != temp_end:  # single number isn't a range
        output.append('{}->{}'.format(temp_start, temp_end))

    return output

if __name__ == '__main__':
    import unittest

    class TestRanges(unittest.TestCase):
        def test1(self):
            """
            Tests a basic input that should only have 1 element in the list
            :return:
            """
            self.assertEqual(ranges([1, 2]), ['1->2'])

        def test2(self):
            """
            Tests a case in which the return value should contain no elements
            :return:
            """
            self.assertEqual(ranges([1]), [])

        def test3(self):
            self.assertEqual(ranges([1, 2, 3, 4, 5, 8, 9, 10]), ['1->5', '8->10'])

        def test4(self):
            self.assertEqual(ranges([5, 6, 7, 20, 21, 22, 25]), ['5->7', '20->22'])

        def test5(self):
            self.assertEqual(ranges([5, 6, 9, 10, 12, 13, 15, 16, 18, 19, 25, 30]),
                             ['5->6', '9->10', '12->13', '15->16', '18->19'])

        def test6(self):
            self.assertEqual(ranges([5, 6, 7, 10, 15, 18, 20, 21, 22]), ['5->7', '20->22'])

    unittest.main()
