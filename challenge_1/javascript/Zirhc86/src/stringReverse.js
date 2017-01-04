
console.log('Running test() with no argument will log \'Example string!\' reversed.'); 
/*
 ********************************************************************
 ************************CHALLENGE ANSWER ***************************
 ********************************************************************/
function reverseString(stringToReverse) {
	var reversedString = "";
	// Run throught chars of string backward, adding to reversedString
 	for(var i = stringToReverse.length - 1; i >= 0; i--){
 		reversedString += stringToReverse.charAt(i);
 	}
 	return reversedString;
}

/********************************************************************
*********************************************************************
*********************************************************************/


// Test function. Logs default string if no string is passed when called
function test(testString){
	if(testString){
		console.log(reverseString(testString));
	}
	else{
		console.log(reverseString('Example string!'));
	}
}