import sys

if __name__ == "__main__":
    # Read in all inputs
    input = sys.argv[1:]
    # Join list of inputs into a string
    input_string = " ".join(input)
    # Reverse now
    reverse_string = input_string[::-1]
    # Print
    print reverse_string
