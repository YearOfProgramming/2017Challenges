def get_len(_int):
    '''Find the number of digits of an int
    if not mathematical integer (1.0 allowed)
    (e.g. 1.1), return -1

    Given an integer, finds the number of
    digits in that integer in base 10
    '''
    power = 0

    if _int % 1 != 0:
        return -1

    while True:
        if _int < 10**power:
            return power
        power += 1

def is_palindrome(_int):
    len_pre = get_len(_int)

    # base cases
    if len_pre == -1:
        # e.g. 4323.4 (refer func get_len)
        return False
    elif len_pre == 0 or len_pre == 1:
        # e.g. 0, 1, 2, ...
        return True
    elif len_pre == 2:
        # e.g. 11, 22, 33, ...
        return _int % 11 == 0

    # recursive reduction
    else:
        digit_last = _int % 10
        _int -= digit_last
        _int /= 10
        _int -= digit_last * 10**(len_pre-2)

        # check for extra zeroes
        # e.g. 1010101 -> return 101 NOT 1010
        len_post = get_len(_int)
        if len_pre - len_post < 2:
            return False
        elif len_pre - len_post > 2:
            extra_0 = len_pre - len_post - 2
            _int /= 10**extra_0

    return is_palindrome(_int)


def is_palindrome_str(_str):
    return is_palindrome(int(_str))

if __name__ == '__main__':
    while True:
        print(is_palindrome_str(input(' >>> ')))

'''
# FOR REPL.IT
while True:
    print(is_palindrome_str(input(' >>> ')))
'''

