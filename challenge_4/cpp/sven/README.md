#Challenge_4 Solution

Under Windows - using the Visual studio c++ compiler:
To compile, run: "cl.exe src\Invert.cpp" 
and run the resulting file with your tree as arguments in preorder position with null termination as '#' sign
For example: "Invert.exe 4 2 1 # # 3 # # 7 6 # # 9 # #". encodes the example tree given for challenge 4
and "Invert.exe P F B # # H G # # # S R # # Y T # W # # Z # #" encodes the tree as shown here: http://jcsites.juniata.edu/faculty/rhodes/cs2java/images/btreeTrav2.gif

cl can be found in C:\Program Files (x86)\<Visual Studio folder>\VC\bin
(e.g. C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin)
or you can open a visual studio command prompt which adds the correct paths to its environment.

Under Linux - using the gcc compiler:
g++ src\Invert.cpp && a.out
