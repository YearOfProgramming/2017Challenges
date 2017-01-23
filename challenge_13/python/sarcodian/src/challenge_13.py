def int_palin():
    '''
    Asks for a input of a int. If the int is a palindrome,
    returns True, else False
    '''

    while True:
        try:
            x = int(input("Please enter your int: "))
            break
        except ValueError:
            print("Not an int")
    y = x
    lenght_x = 0
    
    while y:
        lenght_x += 1
        y = y // 10
        
    loop = lenght_x
    
    for i in range(lenght_x//2):
        if (x % 10) == x // (10**(loop-1)):
            loop -= 2
            x = x // 10
            x = x % (10**loop)
        else:
            return False
    
    return True