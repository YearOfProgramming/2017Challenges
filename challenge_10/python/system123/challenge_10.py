from math import floor 

def check_closers(input_str):
    OPENS  = ('(', '<', '[', '{')
    CLOSES = (')', '>', ']', '}')
    
    expected = []
    valid = True

    for char in input_str:
    	if char in OPENS:
    		idx = OPENS.index(char)
    		expected.append(CLOSES[idx])
    	elif char in CLOSES:
    		if expected and char == expected[-1]:
    			expected.pop()
    		else:
    			valid = False
    			break

    if len(expected) > 0:
    	valid = False

    return(valid)
