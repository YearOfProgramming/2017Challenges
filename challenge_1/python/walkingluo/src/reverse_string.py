#
# Reverse a String
#


def reverse_string(input_str):
    return input_str[::-1]


if __name__ == '__main__':
    input_str = "hello"
    reverse_str = reverse_string(input_str)
    print(reverse_str)
