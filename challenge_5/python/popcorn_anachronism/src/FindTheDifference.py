class Solution(object):
    def findTheDifference(self, s, t):
        s_freq={} #dict for freqs of chars in s
        t_freq={} #dict for freqs of chars in t
        #populate s_freq
        for i in range(len(s)):
            if s[i] in s_freq:
                s_freq[s[i]] += 1
            else:
                s_freq[s[i]] = 1
        #populate t_freq
        for j in range(len(t)):
            if t[j] in t_freq:
                t_freq[t[j]] += 1
            else:
                t_freq[t[j]] = 1
        #check if t_freq matches s_freq, returns first anomaly
        for j in range(len(t)):
            if t[j] not in s_freq or s_freq[t[j]] != t_freq[t[j]]:
                return t[j]
        return

#standalone testing
#Test = Solution()
#print(Test.findTheDifference("abcd", "abcde"))
