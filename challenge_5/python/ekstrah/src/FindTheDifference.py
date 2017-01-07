class Solution(object):
    def findTheDifference(self, s, t, default=None):
        sList = list(s)
        tList = list(t)
        for rm in sList:
            tList.remove(rm)
        # print(tList[0])
        if len(tList) == 0:
        	return default
        else:
        	return tList[0]
