#Challenge #12, Compression and Decompression I

Our solution comes in two parts, `compress` and `decompress`. Running `challenge_12.py` will invoke an 'interactive' mode that will compress or decompress according to the input.

`compress`,

1. The main logic in this function is to iterate through characters of the given input string, and compare it to the previous character to determine if it is a different character.
2. If it is a different character, we will examine how many times the previous character was repeated.
3. If there are greater than 4 repetitions, we append to the output string `compressed` in the given format {character}#{repetitions}. Otherwise, simply append with no changes.
4. To facilitate this, we store iterated strings in a buffer list `buff`. This list is reset after each application of the logic in (3).

Some minor features:

* The first character is added to the buffer before the iterating `for` loop to prevent `IndexError` for the comparison conditional detecting change in character `if character == buff[-1]`.
* There is a `else` for the main iterating `for` loop for the case whereby the string ends on a sequence of repeats (and therefore there is no differing character to trigger `elif character != buff[-1]`

`decompress`,

1. The main logic in this function is to iterate through the characters of the given input string, and append all alphabetical characters into the output string.
2. Numerical characters are held until they are followed by an alphabet (in the case of numbers greater than 9), after which an appropriate number of repetitions of the last alphabet is appended tot he output.

Some minor features:

* The '#' character is removed at the start as it serves no purpose (numbers are sufficient to indicate a sequence of compressed repetition).
* As with `compress`, an `else` block for the main iterating `for` loop catches the case whereby the input string ends in a number.
