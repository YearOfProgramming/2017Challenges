# should work with both python2 and python3

def findSingleton(sList):
    """ Returns entries that only occured once in list """

    # Count dict is used for storing if we've seen a element
    # and how many times it occured
    count_dict = {}
    # Single dict is used for storing which elements we've seen only once
    single_dict = {}

    # Iterate over every key in our list
    for key in sList:
        # If the key exists in our count dict
        if key in count_dict.keys():
            # count up
            count_dict[key] += 1
            # remove element from single dict
            single_dict.pop(key, None)
        else:
            #initiate key in both dicts
            count_dict[key] = 1
            single_dict[key] = True

    # return the keys in dict
    return single_dict.keys()
