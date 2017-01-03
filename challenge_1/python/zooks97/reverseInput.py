inText = input("Input some characters: ") #Get the text input

listText = list(inText)			#Convert the input string to a list
listText.reverse()			#Reverse the character list
outText = ''.join(listText)		#Revert list to string

print(outText)	#Print reversed string
