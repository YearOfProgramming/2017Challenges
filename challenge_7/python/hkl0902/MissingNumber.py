class MissingNumber:
    def __init__(self, lst):
        self.numbers = lst

    def findMissingNum(self):
        n = len(self.numbers)
        completeTotal = n*(n+1)/2
        return completeTotal - sum(self.numbers)
