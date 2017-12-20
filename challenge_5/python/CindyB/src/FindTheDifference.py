class Solution:

    def findTheDifference(self,s,t):
        letter_dict = dict()

        for letter in s:
            if letter_dict.has_key(letter):
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
        
        for letter in t:
            if letter_dict.has_key(letter):
                letter_dict[letter] -= 1
                if letter_dict[letter] == 0:
                    del letter_dict[letter]
            else:
                return letter