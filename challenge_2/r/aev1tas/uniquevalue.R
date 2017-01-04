input <- c(2,"a","l",3,"l",4,"k",2,3,5,4,"a",6,"c",4,"m",6,"m","k",9,10,9,8,7,8,10,7)
tab.input <- table(input[!is.na(as.numeric(input))])
names(tab.input)[tab.input <= 1]
