from collections import Counter
import time

class Solution(object):
    def findTheDifference_old(self, s, t):
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

    def findTheDifference(self, s, t):
        s_count = Counter(s)
        t_count = Counter(t)
        for letter in t_count:
            if t_count[letter] != s_count[letter]:
                return letter
        return

#standalone testing
Test = Solution()
start1 = time.clock()
print(Test.findTheDifference("abcd", "abcde"))
print("Test1 - Counter: %.5f seconds" % (time.clock()-start1))

start1 = time.clock()
print(Test.findTheDifference_old("abcd", "abcde"))
print("Test1 - dicts: %.5f seconds" % (time.clock()-start1))

start2 = time.clock()
print(Test.findTheDifference("asldfkjasdflkjasdlkfjaslkjasdlfkasjflaksjdflaksdjfslfkjalsdkfjalsdkfjasldkfjsalfkjadsldskfjsalfkdjflakfjdlaskdfjsaldkfjsaldkfjasldkfjasldkfjasldfkjasldfkjasldfkjasdflkwejfqiuvfdlskfjlasdkfjlfkdsjflsafjslkfjeoiruqwpeoruiqeioqwolkfjasldkfjalsdvkjlxkvjzldkfjsdfoiajfwoperqueriwsflkajdlfvkjxlfkjasodfiqpweoifjasldkfjlvkjxvboxkjsadofidjawleksdfjxovcibjxlfkgjaofiawjesflkdjvbxcoijalsdfkjqweoifasjdlfkjfvlbxkjlskfjalsdkfjalwdkfjalkej1231233alsdkfjsaldkfjlkjwoeifjlskjvxcnmvs,dfaksdjfaweilfjalsdkff", "asldfkjasdflkjasdlkfjaslkjasdlfkasjflaksjdflaksdjfslfkjalsdkfjalsdkfjasldkfjsalfkjadsldskfjsalfkdjflakfjdlaskdfjsaldkfjsaldkfjasldkfjasldkfjasldfkjasldfkjasldfkjasdflkwejfqiuvfdlskfjlasdkfjlfkdsjflsafjslkfjeoiruqwpeoruiqeioqwolkfjasldkfjalsdvkjlxkvjzldkfjsdfoiajfwoperqueriwsflkajdlfvkjxlfkjasodfiqpweoifjasldkfjlvkjxvboxkjsadofidjawleksdfjxovcibjxlfkgjaofiawPjesflkdjvbxcoijalsdfkjqweoifasjdlfkjfvlbxkjlskfjalsdkfjalwdkfjalkej1231233alsdkfjsaldkfjlkjwoeifjlskjvxcnmvs,dfaksdjfaweilfjalsdkff"))
print("Test2 - Counter: %.5f seconds" % (time.clock()-start2))

start2 = time.clock()
print(Test.findTheDifference_old("asldfkjasdflkjasdlkfjaslkjasdlfkasjflaksjdflaksdjfslfkjalsdkfjalsdkfjasldkfjsalfkjadsldskfjsalfkdjflakfjdlaskdfjsaldkfjsaldkfjasldkfjasldkfjasldfkjasldfkjasldfkjasdflkwejfqiuvfdlskfjlasdkfjlfkdsjflsafjslkfjeoiruqwpeoruiqeioqwolkfjasldkfjalsdvkjlxkvjzldkfjsdfoiajfwoperqueriwsflkajdlfvkjxlfkjasodfiqpweoifjasldkfjlvkjxvboxkjsadofidjawleksdfjxovcibjxlfkgjaofiawjesflkdjvbxcoijalsdfkjqweoifasjdlfkjfvlbxkjlskfjalsdkfjalwdkfjalkej1231233alsdkfjsaldkfjlkjwoeifjlskjvxcnmvs,dfaksdjfaweilfjalsdkff", "asldfkjasdflkjasdlkfjaslkjasdlfkasjflaksjdflaksdjfslfkjalsdkfjalsdkfjasldkfjsalfkjadsldskfjsalfkdjflakfjdlaskdfjsaldkfjsaldkfjasldkfjasldkfjasldfkjasldfkjasldfkjasdflkwejfqiuvfdlskfjlasdkfjlfkdsjflsafjslkfjeoiruqwpeoruiqeioqwolkfjasldkfjalsdvkjlxkvjzldkfjsdfoiajfwoperqueriwsflkajdlfvkjxlfkjasodfiqpweoifjasldkfjlvkjxvboxkjsadofidjawleksdfjxovcibjxlfkgjaofiawPjesflkdjvbxcoijalsdfkjqweoifasjdlfkjfvlbxkjlskfjalsdkfjalwdkfjalkej1231233alsdkfjsaldkfjlkjwoeifjlskjvxcnmvs,dfaksdjfaweilfjalsdkff"))
print("Test2 - dicts: %.5f seconds" % (time.clock()-start2))

start3 = time.clock()
print(Test.findTheDifference("", ""))
print("Test3 - Counter: %.5f seconds" % (time.clock()-start3))

start3 = time.clock()
print(Test.findTheDifference_old("", ""))
print("Test3 - dicts: %.5f seconds" % (time.clock()-start3))
