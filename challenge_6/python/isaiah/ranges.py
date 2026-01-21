def ranges(list):
    ranges_found = []    
    if(len(list) < 2):
        return ranges_found
        
    start = list[0]
    range_count = 1
        
    for i in range(0, len(list) - 1):
        if(list[i+1] != list[i] + 1):
            # Append range if it's longer than one number
            if(range_count > 1):
                ranges_found.append(str(start) + "->" + str(list[i]))
            range_count = 0
            start = list[i+1]
            
        range_count += 1
      
    # Append last number if it's part of the range    
    if(list[len(list)-1] == list[len(list)- 2] + 1):
        ranges_found.append(str(start) + "->" + str(list[len(list)-1]))

        
    return ranges_found