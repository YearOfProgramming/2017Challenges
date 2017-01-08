while (TRUE) {
  
  if (interactive () ) {
    strinput <- readline(prompt="Type or paste numbers separated by commas to verify \nwhat is the majority element, if any. Type 'quit' to quit: ")
  }
  else{
    cat("Type or paste numbers separated by commas to verify \nwhat is the majority element, if any. Type 'quit' to quit: ")
    strinput <- readLines("stdin",n=1)
  }
  
  if (strinput == "quit") {
    break
  }
  strinput <- gsub("\\[|\\]","",strinput) 
  #People with some knowledge of arrays might want to
  #write them in brackets, but that would upend the tabulation
  strinput <- as.vector(strsplit(as.character(strinput), split=","))
  threshold <- floor(length(strinput[[1]])/2)
  tabinput <- as.data.frame(table(strinput))
  if(nrow(tabinput[tabinput$Freq>threshold,])>0){
    print(paste0("Your majority element is ", tabinput[tabinput$Freq>threshold,]$strinput[1]))
  } else{
    print("Your array does not have a majority element")
  }
}
