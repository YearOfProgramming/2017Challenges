# Integer Palindrome

def is_palindrome(num):
    """
    Returns True if integer is a Palindrome
    """
    num = [int(x) for x in str(num)]
    digits = len(num)
    mid = digits // 2
    back_half = num[mid:]

    if digits % 2 == 0:
        return True if num[:mid] == back_half[::-1] else False

    else:
        return True if num[:mid+1] == back_half[::-1] else False


if __name__ == "__main__":

    num = int(input())
    print()
    print(is_palindrome(num))
