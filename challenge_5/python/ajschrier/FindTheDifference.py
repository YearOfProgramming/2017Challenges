from collections import Counter


class Solution():
    def findTheDifference(self, s, t):
        sCounter = Counter(s)
        tCounter = Counter(t)
        for i in tCounter:
            if tCounter[i] > sCounter[i]:
                return i


def main():
    s = "abcd"
    t = "abcde"
    a = Solution()
    print a.findTheDifference(s, t)


if __name__ == '__main__':
    main()
