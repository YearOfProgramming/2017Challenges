class Solution(object):
    def findTheDifference(self, s, t):
        sList = list(s)
        tList = list(t)
        for rm in sList:
            tList.remove(rm)
        # print(tList[0])
        return tList[0]
