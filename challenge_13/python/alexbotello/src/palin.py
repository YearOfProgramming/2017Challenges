# Integer Palindrome

def is_palindrome(num):
    """
    Returns True if integer is a Palindrome
    """
    reverse = 0
    num2 = num

    while num2 > 0:
        # Finds the last digit of num2, removes it, and adds the
        # digit to the reverse variable
        reverse = (10*reverse) + num2%10
        num2 //= 10

    return True if reverse == num else False

if __name__ == "__main__":
    num = int(input())
    print()
    print(is_palindrome(num))
