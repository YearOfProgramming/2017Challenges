def check_close(input_string):
    OPENS  = ('(', '<', '[', '{')
    CLOSES = (')', '>', ']', '}')
    PAREN  = ('(', ')')
    ANGLE  = ('<', '>')
    SQUARE = ('[', ']')
    CURLY  = ('{', '}')
    mem = []

    for character in input_string:
        try:
            if character in OPENS:
                mem.append(character)
            elif character in CLOSES:
                if   (character in PAREN and
                      mem[-1] in PAREN):
                      del mem[-1]
                elif (character in ANGLE and
                      mem[-1] in ANGLE):
                      del mem[-1]
                elif (character in SQUARE and
                      mem[-1] in SQUARE):
                      del mem[-1]
                elif (character in CURLY and
                      mem[-1] in CURLY):
                      del mem[-1]
                else:
                    return False
        except IndexError:
            return False

    if mem == []:
        return True
    else:
        return False

if __name__ == '__main__':
    while True:
        print(check_close(input(' >>> ')))
