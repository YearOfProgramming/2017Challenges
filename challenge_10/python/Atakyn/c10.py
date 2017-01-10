# determine if ( { and [ are all closed correctly


def valid_closers(s):
    parenthesis = 0
    braces = 0
    brackets = 0
    for c in s:
        if c == '(':
            parenthesis += 1
        elif c == ')':
            parenthesis -= 1
        elif c == '{':
            braces += 1
        elif c == '}':
            braces -= 1
        elif c == '[':
            brackets += 1
        elif c == ']':
            brackets -= 1

        if parenthesis < 0 or braces < 0 or brackets < 0:  # someone closed before opening
            return False

    if parenthesis == 0 and braces == 0 and brackets == 0:  # zero means as many openings as closings
        return True
    else:
        return False

print(valid_closers(input('Input the strings to test: ')))
