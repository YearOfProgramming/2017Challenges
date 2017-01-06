if __name__ == '__main__':
    phrase = input()
    print(''.join([phrase[len(phrase)-i-1] for i in range(len(phrase))]), end='')
    print()
