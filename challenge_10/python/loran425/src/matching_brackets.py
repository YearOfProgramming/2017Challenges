__author__ = "Loran425"


def matching_brackets(str):
    # O(1) space complexity beyond the input string
    interesting = '(){}[]'
    opening = '({['
    closing = ')}]'
    brackets = 0
    braces = 0
    parenth = 0

    for char in str:  # O(n) time complexity
        if char in interesting:  # only evaluate interesting characters since they cost 6 checks

            if char in opening:
                if char is '(':
                    parenth += 1
                elif char is '{':
                    braces += 1
                elif char is '[':
                    brackets += 1

            elif char in closing:
                if char is ')':
                    parenth -= 1
                elif char is '}':
                    braces -= 1
                elif char is ']':
                    brackets -= 1
                if braces < 0 or brackets < 0 or parenth < 0:  # Break for out of order designators
                    return False

    if braces == 0 and brackets == 0 and parenth == 0:
        return True

    return False
