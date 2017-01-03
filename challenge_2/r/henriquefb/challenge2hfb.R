while (TRUE) {
  
  if (interactive () ) {
    strinput <- readline(prompt="Type or paste an array of numbers. Type 'quit' to quit: ")
  }
  else {
    cat("Type or paste an array of numbers. Type 'quit' to quit: ")
    strinput <- readLines("stdin",n=1)
  }
  
  if (strinput == "quit") {
    break
  }
    
  strinput <- as.character(strinput)
  
  strinput <- substring(strinput, seq(1,nchar(strinput),1), seq(1,nchar(strinput),1))
  
  tabinput <- as.data.frame(table(strinput))
  
  uniqchar <- tabinput[tabinput$Freq==1,]
  
  if (nrow(uniqchar)==0) {
    print("There are no unique entries in your array.")
  }
  
  else {
    print(paste0("The unique entries in your array are: ", paste(as.character(uniqchar$strinput), collapse=",")))
  }
}
