# -*- coding: utf-8 -*-
#@author: Shaowen Liu

import re

def replace_fun(match):
    duplicated = match.group()
    return '%s#%d' % (duplicated[0], len(duplicated))

def replace_fun2(match):
    compressed = match.group()
    return compressed[0] * int(compressed[2:])

def compress(astring):
    """compress string"""
    pattern = re.compile(r'(([a-zA-Z])\2{3,})')
    
    return pattern.sub(replace_fun, astring)

def decompress(astring):
    """decompress string"""
    pattern = re.compile(r'(\w#\d+)')
    
    return pattern.sub(replace_fun2, astring)

if __name__ == '__main__':
    astring = raw_input('Input string:')
    
    if '#' in astring:
        decompress_str = decompress(astring)
        print 'Decopressed string:\n%s\n' % decompress_str
    else:
        compress_str = compress(astring)
        print 'Compressed string: \n%s\n' % compress_str
    
    
    