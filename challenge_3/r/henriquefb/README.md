1. Short description

This algorithm receives as input an unordered array of numbers,
and yields, if any, the majority element. The majority element
is, by definition, the one that appears more than ⌊ n/2 ⌋ times, 
where n is the size of the array. The input array can be in brackets
or not, but the numbers must be separated by commas. The elements
can be numeric or strings. 

2. Executing the code

The code should run in R's interactive mode (directly from R/Rstudio),
or straight from an Unix terminal, using Rscript. 

3. Execution examples

input: 3,4,2,1,

output: [1] "Your array does not have a majority element"

input: 2,2,2,2,2,1

output: [1] "Your majority element is 2"

input: [a,a,a,a,2]

output: [1] "Your majority element is a"
