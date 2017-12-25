# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:21:20 2017
"""
def solution(strr):
    """check if all brackets closed properly"""
    
    closerof = {'{':'}', '[':']','(':')'}
    START = ('[','{','(')
    CLOSE = (']','}',')')
    stack = []
    
    for i in strr:
        # push into stack, if new bracket found
        if i in START:
            stack.append(i)
        # pop out if proper closer found, else False
        elif i in CLOSE:
            if closerof[stack[-1]] == i:
                stack.pop()
            else:
                return False
               
    # check leftover in stack
    return not stack