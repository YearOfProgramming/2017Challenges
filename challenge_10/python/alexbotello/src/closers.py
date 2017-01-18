# Valid Closers

def is_valid_closer(string):
    """
    Returns True if every opener has a valid closer
    """
    openers = ['[', '(', '{']
    closers = [']', ')', '}']
    stack = []

    for ch in string:
        # If there is a closer, but no openers
        if not stack and ch in closers:
            return False

        # Add any opener into the stack
        elif ch in openers:
            stack.append(ch)

        # If the following closers do not pair with the opener popped from stack
        # then the function will return False
        elif ch == ']':
            if stack.pop() != '[':
                return False

        elif ch == ')':
            if stack.pop() != '(':
                return False

        elif ch == '}':
            if stack.pop() != '{':
                return False

    # Nothing in our stack == True
    return not stack
