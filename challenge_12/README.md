Compression and Decompression I
======
Idea
------
No doubt you've heard the word "compression" before. Compression is a massive concept in computing and crucial for transferring large files quickly. A lot of popular file transfer services don't even let you transfer something if it's not in a .zip file these days.

Your job today is to create a program capable of doing two things. Compressing strings and decompressing them. Your program only needs to be able to handle text so don't worry about binary. Your "compress" method will take in a string and scan it for characters in tandem with the same character. Anytime you encounter a sequence of 4 or more identical characters all but one of those characters should be replaced with #[num of characters]. For example 'aaaaa' has 5 a's. Our compression function would turn that string into 'a#5'. 

As for decompressing, your program needs to be capable of uncompressing the compressed string.

Notes
* The input will never be empty
* The input can consist of any (printable) character
* The input can be of any length
* You may not be able to compress the input at all, ex: 'abc'

Testing
-----
Testing for this program is fairly straight forward. Simply think of a few strings, some that can be compressed, some that can't and feed it into your compression function. Once you have verified that it is compressed correctly, feed it into your decompress function. All you have to do now is compare the output of the decompressed function with the initial string and you will have your answer as to whether or not it decompressed properly.