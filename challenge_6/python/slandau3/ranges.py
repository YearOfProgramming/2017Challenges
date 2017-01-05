#!/usr/bin/env python3
# @author Slandau3

def ranges(input: list) -> list:
    # The patterns_found list keeps track of the definite ranges we have completed
    patterns_found = []
    # pattern_in_progress keeps track of a pattern we are tracing
    pattern_in_progress = []

    for i in input:
        if len(pattern_in_progress) == 0: # Add the beginning of the input to the pattern_inprogress list
            pattern_in_progress.append(i)
        elif i == pattern_in_progress[-1]+1:
            # If the integer we are currently looking at is the same as the previous number
            # in pattern_in_progress +1, then we know the range will continue
            pattern_in_progress.append(i)
        else:
            # If you're here than we found an integer that is not the previous integer + 1
            if pattern_in_progress[0] == pattern_in_progress[-1]: # Case for two "rangeless" integers in order
                # ex: 1, 2, 3, 14, 25, 30, 31, 32
                pattern_in_progress = [i]
                continue # ends this iteration of the loop

            # The fact that we have gotten this far means we are ready to add the range to the patterns_found list
            patterns_found.append("{num1}->{num2}".format(num1=pattern_in_progress[0], num2=pattern_in_progress[-1]))
            pattern_in_progress = [i]

    if len(pattern_in_progress) > 1:
        # This if statement ensures that a range that was in progress when the loop ended is added to
        # the patterns_found list.
        patterns_found.append("{num1}->{num2}".format(num1=pattern_in_progress[0], num2=pattern_in_progress[-1]))

    return patterns_found


if __name__ == '__main__':
    ranges(list(input()))