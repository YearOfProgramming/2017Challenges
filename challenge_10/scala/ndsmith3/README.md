# Valid Closers
---
- Pattern matches input String
- Uses stack to keep track of brackets
- Uses closure to prevent needlessly converting string to `List[Char]`

This algorithm scans through the string. When it encounters an opening
bracket, it pushes it onto a stack. When it encounters a closing bracket, it
checks the top of the stack to see if it matches the closing bracket. If it
does, the stack gets popped, otherwise the algorithm returns false. When the
entire string has been scanned, if the stack is empty, the algorithm returns
true, if not, it returns false.
