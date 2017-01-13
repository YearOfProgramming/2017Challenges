#!/usr/bin/env python3

import re

COMPRESSION_CUTOFF = 3


def compress(string_to_compress: str) -> str:
    output = ""  # The compressed string that will be outputted
    character = ""  # character the string_to_compress at blank
    occurrences = 0  # the number of occurrences of this letter
    for index, char in enumerate(string_to_compress):  # goes through both the range and the characters at the same time
        if char != character or index == len(string_to_compress)-1:  # if we spot a different character,
            # or are at the end of the string_to_compress
            # go here
            if index == len(string_to_compress)-1 and character == char:  # If we are at the end of
                # the string_to_compress
                # but the last character is the same, add to the occurrences of the character
                occurrences += 1

            if occurrences > COMPRESSION_CUTOFF:
                # If we have more than three occurrences, add the compress format to the output
                output += character + '#' + str(occurrences)
            else:
                # the next line puts 'occurrences' number of 'character' in the output
                output += character * occurrences

            if index == len(string_to_compress)-1 and character != char:
                # If we are at the end of the string_to_compress and the character
                # is not the same as the last. Top it off
                output += char

            character = char # set char to character so we know the last character we looked at
            occurrences = 1

        else:
            occurrences += 1

    return output


def decompress(string_to_uncompress: str) -> str:
    # Using regular expressions to parse the string_to_uncompress
    matches = re.findall(r'(.#\d+)', string_to_uncompress) # Looking for [anything]#[at least one number]
    decompressed = string_to_uncompress # decompressed is the new string that we will output
    for match in matches: # Scan through the matches and uncompress each of them
        # match the character so we know what character we need to expand
        char = re.match(r'(.)#\d+', match)
        # Determine the number of times it occurred
        times = re.search(r'(\d+)', match)

        replacement = char.group(1) * int(times.group(1)) # To get the matches specifically we need to access
        # them at group 1
        decompressed = decompressed.replace(match, replacement)

    return decompressed


print(decompress(compress("aaaaaaaa")))
