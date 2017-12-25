def compress(strr):
    buff = []
    compressed = ''

    buff.append(strr[0])
    for character in strr[1:]:
        if character == buff[-1]:
            buff.append(character)
        elif character != buff[-1]:
            if len(buff) > 4:
                compressed += '{c}#{n}'.format(
                        c=buff[-1],
                        n=len(buff)
                        )
            else:
                compressed += ''.join(buff)
            buff = [character]
    else:
        if len(buff) > 4:
            compressed += '{c}#{n}'.format(
                    c=buff[-1],
                    n=len(buff)
                    )
        else:
            compressed += ''.join(buff)
        buff = [character]
    
    return compressed

def decompress(strr):
    strr = strr.replace('#', '')
    repeats = ''
    decompressed = ''
    NUMS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    for character in strr:
        if character not in NUMS:
            if repeats != '':
                decompressed += decompressed[-1] * (int(repeats)-1)
                repeats = ''
            decompressed += character
        else:
            repeats += character
    else:
        if repeats != '':
            decompressed += decompressed[-1] * (int(repeats)-1)
            repeats = ''


    return decompressed

def main():
    strr = input(' >>> ')
    if '#' in strr:
        print(decompress(strr))
    else:
        print(compress(strr))

if __name__ == '__main__':
    while True:
        main()

'''repl.it
as i understand, repl.it does not do
__name__ == '__main__', so here's
the equivalent:'''

'''
while True:
    main()
'''

