class Solution:
    def findTheDifference(self, s, t):
        """
        :param s: String
        :param t: String
        :return:  String
        """

        #Turn strings into sorted lists
        sList = sorted(s)
        tlist = sorted(t)

        #enumerate over ever char in tList. If it isn't equal to the same spot in sList then it was added
        for index,val in enumerate(tlist):
            #If last value is the character aded
            if index > len(sList) - 1:
                return val
            elif val != sList[index]:
                return val
