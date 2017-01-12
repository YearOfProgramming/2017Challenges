import unittest
from challenge9 import square, merge, challenge9, get_break_index


class Tests(unittest.TestCase):

    def test1(self):
        '''
        Tests that square takes a list and squares all the inputs, returning them as a list
        :return:
        '''
        self.assertEqual(square([-1,0,4]),[1,0,16])


    def test2(self):
        '''
        Tests that merge will return a sorted list combining two relatively sorted lists
        :return:
        '''
        self.assertEqual(merge([0,1,2,3],[4,5,6]), [0,1,2,3,4,5,6])

    def test3(self):
        '''
        Test to make sure that get_break returns the index of the first pos number in a list
        :return:
        '''
        self.assertEqual(get_break_index([-4,-1,0,3,5,6]),3)

    def test4(self):
        '''
        Tests that challenge9 will produce the correct output for a sorted list that is squared and then resorted
        '''
        self.assertEqual(challenge9([-3,-2,0,3,4,6]),[0, 4, 9, 9, 16, 36])

if __name__ == '__main__':
    unittest.main()