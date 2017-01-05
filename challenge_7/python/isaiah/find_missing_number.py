def find_missing_number(list):
    n = len(list)
    # Find correct total using summation of first n natural numbers
    correct_total = (n*(n+1))//2
    
    actual_total = 0
    # Count the total in the list
    for i in list:
        actual_total += i
        
    return correct_total - actual_total