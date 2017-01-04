
console.log('Running test() with no argument will log \'Example string!\' reversed.');

/*
 ********************************************************************
 ************************CHALLENGE ANSWER ***************************
 ********************************************************************/
function reverseString(stringToReverse) {
	return stringToReverse.split('').reverse().join('');
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