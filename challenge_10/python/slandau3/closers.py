#!/usr/bin/env python3
# @author slandau3


def valid_closers(string_with_brackets_in_it_or_maybe_not_idk_i_coudnt_think_of_a_name: str) -> bool:
    stack = [] # initialize an empty list (which can easily be used as a stack in python)

    closers = [']', ')', '}']
    openers = ['{', '(', '[']
    for char in string_with_brackets_in_it_or_maybe_not_idk_i_coudnt_think_of_a_name:
        if len(stack) == 0 and char in closers:
            # This if statement will return false if there is no open bracket to match the closing bracket.
            # More specifically it returns false if the list is null and we have recieved a closer
            return False

        if char in openers:
            stack.append(char)

        elif char == '}':
            if stack.pop() != '{':
                return False

        elif char == ']':
            if stack.pop() != '[':
                return False

        elif char == ')':
            if stack.pop() != '(':
                return False

    return True if len(stack) == 0 else False


if __name__ == '__main__':
    print(valid_closers('{{{{{{{{{[[[[[[kadfa{{{{{{{((({daljfdaf({{{[]}}kaldjfs})})))}}}}}}}]]]]]]}kjfela}}}}}}}}'))