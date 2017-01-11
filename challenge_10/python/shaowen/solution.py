# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:21:20 2017

@author: Shaowen Liu
"""
def solution(strr):
    """check if all brackets closed properly"""
    
    closerof = {'{':'}', '[':']','(':')'}
    stack = []
    
    for i in list(strr):
        # push into stack, if new bracket found
        if i in ['[','{','(']:
            stack.append(i)
        # pop out if proper closer found, else False
        elif i in [']','}',')']:
            if closerof[stack[-1]] == i:
                stack.pop()
            elif closerof[stack[-1]] !=i:
                return False
    # check leftover in stack
    if stack:
        return False
    else:
        return True