def get_int_len(_int):
    '''Find the number of digits of an int

    Given an integer, finds the number of
    digits in that integer in base 10
    '''
    power = 1
    while True:
        if _int == 0:
            return 0
        elif _int < 10**power:
            return power
        power += 1

def check_palindrome(_int):
    ones = 0
    digits = get_int_len(_int)
    while digits > 1:
        if _int % 10 != 0:  # not end with 0
            ones += 1
            _int -= 1
        else:
            _int -= ones * 10**(digits-1)
            _int /= 10
            new_digits = get_int_len(_int)
            diff_digits = digits - new_digits
            if diff_digits == 1 or _int < 0:
                # e.g. 514, 510, 110, 10
                # e.g. 415, 410, -90, -9
                return False
            elif diff_digits > 2:
                # e.g. 10101, 10100, 0010
                extra_zeroes = diff_digits - 2
                _int /= 10**(extra_zeroes)
                if _int % 1 != 0:
                    return False
            digits = get_int_len(_int)
            ones = 0

    return True

def check_palindrome_str(_str):
    return check_palindrome(int(_str))

if __name__ == '__main__':
    while True:
        print(check_palindrome_str(input(' >>> ')))

'''
# FOR REPL.IT
while True:
    print(check_palindrome_str(input(' >>> ')))
'''

