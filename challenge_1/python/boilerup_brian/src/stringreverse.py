#input a string to reverse
toreverse = input('Input a string to be reversed: ');

reversed = ''

for i in range(1, len(toreverse) + 1):
    reversed += toreverse[len(toreverse) - i]
    
print('%s\n' %reversed)
