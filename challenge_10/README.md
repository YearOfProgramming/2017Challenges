Valid Closers
=======
Idea
----
This problem is a classic. Given a string that contains various amounts of { [ or (, your job is to determine if each of these are closed successfully. Every { must have a }, every [ must have a ], and every ( must have a ). Any characters can appear between any of these. If the string does have valid closers, the program should return True, otherwise it should return false.

Your solution should use a maximum of O(N) space and run in O(N) time (max).

What is the best data structure for this problem?

Please make your program so that it takes input from standard input. System.in for you java folks and input() for you pythonistas.
[Testing](https://github.com/YearOfProgramming/2017Challenges#testing)
------
Instead of describing each test case, I'm just going to list them out here since I'm sure you can imagine what they might be.

{{{{{{{{{adfkjaefia}}}}}}} should return False

{{{{{{{{{[[[[[[kadfa{{{{{{{((({daljfdaf({{{[]}}kaldjfs})})))}}}}}}}]]]]]]}kjfela}}}}}}}} Should return True

{{{[}}}}dafda Should return False

{{{{{{{{{}}}}}}}}} Should return True

[[[[[[[[[kafjalfeianfailfeja;fjai;efa;sfj]]]]]]]]]kjajdain Should return True

< blank > should return True

((((((fjdalfeja((((alefjalisj(())))))))))))d Should return True

)))(((d Should return False

({)} Should return False
