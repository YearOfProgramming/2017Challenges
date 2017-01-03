## Compile
On a *nix system with gcc, run
$gcc reverseInput.c -o 'output.file'

## Run
$./'output.file'

## Explanation
This c program uses putchar and getchar from the stdio header to reverse inputted text.
Each inputted character before an EOF (ctrl+d in most terminals) is put onto a stack.
Characters are then put back out from the top of the stack down.
