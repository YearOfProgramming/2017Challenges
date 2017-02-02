# Find the Difference
###### C++ 11

### 1. Approch to solving the problem

Go through the small/ original string comparing each character with all the characters in the random string. Once the character matches, the character is removed from both strings. This is repeated until all characters are removed from the original. After this is complete there should be only one character left in the large string, that will be the answer.

### 2. How to compile and run this

In Windows - I used the Visual Studio C++ compiler, move to the proper directory and run:

```
cl.exe /EHsc src/Difference.cpp
Difference.exe
```

### 3. How this program works

Given the original string and the random string, the program compares each character from original to the random. Once the character is found both characters are removed from the string. At the end, leaving only one character left in the random string, this is the difference in the strings.
