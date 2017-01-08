#!/bin/bash
#  ^ This is called a shebang (#!) it tells the shell executing this script where to look for an interpretor
#  Dollar signs "$" are used to denote a variable after it has been declared.
#    e.g.  x=7
#          echo $x
#  Would assign the value of 7 to x.  Then echo would print the value of x to standard output (stdout)
#  declare -r is used to declare a constant. $0 is the varialble for the name of the program
#
declare -r USAGE="Usage: $0 [STRING]"
declare -r INVALID_NUM_OF_ARGS="Error: Invalid number of arguments"
#
#  $# refers to the number of arguments passed to our program
#  -ne means not equal
#  >&2 means redirect to stderr
#  echo writes its arguments to an output; default stdout
#
if [ $# -ne 1 ]; then
	echo "$INVALID_NUM_OF_ARGS" >&2
	echo "$USAGE"
	exit 1
fi
input=$1	#the variable input is set to $1 (the variable for the first arguemnt to our program)
string_reversed=$(echo "$input" | rev)	#  This says, in simple terms: set string_reversed to equal what rev returns, when given $input as the input
#                                          What it really says is set string_reversed to the return value of: (the output of (echo "$input") piped into rev) 
echo "The string \"$input\" reversed is:  "
echo $string_reversed
exit 0
