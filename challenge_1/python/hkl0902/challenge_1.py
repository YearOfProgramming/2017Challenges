import sys

'''
Given a string S, returns the reverse of S
'''

def reverse(s):
    r = ""
    for i in range(len(s)):
        r += s[len(s) - i - 1]
    return r

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        print(reverse(args[1]))
    else:
        print("Give me string to reverse")


