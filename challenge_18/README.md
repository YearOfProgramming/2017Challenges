Paths
======
This ones a classic. Today your job is to determine the number of possible paths to traverse a matrix. 

We are going to do this whereas the coordinates begin at the bottom left, 0,0, and end at the top right. You need to create a program that can find all possible paths through the matrix. The program should take one arguement from standard input, the size of the matrix. This will be a single number that will denote an n x n matrix. Your program should output the number of possible paths associated with each matrix.

When traversing the matrix, you may only move up and to the right (not necessarily in that order).
Examples and Testing
-----
Example 1: N = 10. Possible paths: 184756

Example 2: N = 5. Possible paths: 252

Example 3: N = 12. Possible paths: 2704156

Example 4: N = 2. Possible paths: 6. For the sake of the example, here are the paths ['UURR', 'URUR', 'URRU', 'RUUR', 'RURU', 'RRUU'] U = Up, R = Right

Once again, a program like this will have an enormous time complexity so don't bother testing anything larger than say N = 15 (if that).