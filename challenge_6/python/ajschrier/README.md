# Challenge 6 - Integer Range

*Python Version:* 2.7

Finds ranges of integers from an ordered integer list.

## Functions

### outputRange

**Input:** list(integer)
**Output:**list(string)

Checks the list for sequences.

Starts by maintaining the current sequence. If there is a continuation found, store the new end of the sequence. Add the sequence to the output list after continuation breaks, skipping cases where the current sequence is length 1. Return the list of sequences, or an empty list if no sequences exist.
