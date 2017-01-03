# This loop asks user for input and does the reversing job. If input is "quit",
# the loop will exit.
while (TRUE) {
  # Asking for input -- important thing to notice is that R handles user input differently
  # when interactive mode (say, Rstudio) vs. running scripts directly from shell. The next
  # if condition recognizes this and handles both kinds of inputs so program works
  # everywhere.
  if (interactive () ) {
    strinput <- readline(prompt="Write word to be reversed. Type 'quit' to quit: ")
  }
  else{
  cat("Write word to be reversed. Type 'quit' to quit: ");
  strinput <- readLines("stdin",n=1);
  }
  
  # Calculating input length and copying input onto a new variable;
  # this new variable serves as the placeholder on which we will substitute the 
  # reversed letters
  leng <- nchar(strinput)
  newstr <- strinput
  
    # This little loop does the actual reversing job, by picking up every letter
    # of the input in the position "i" and substituting it into the placeholder at
    # the position "leng - i + 1". Ex: If input word has 10 characters, it will pick
    # up the 2nd character and substitute it for the 10 - 2 + 1 = 9th character
    for (i in leng:1) {
      x <- substr(strinput, i,i)
      substr(newstr, leng - i + 1, leng - 1 + 1) <- x
    }
  
  # Printing the result of the reversing to the terminal or quiitting if input is "quit"
  if (newstr == "tiuq") break else print(newstr)
}