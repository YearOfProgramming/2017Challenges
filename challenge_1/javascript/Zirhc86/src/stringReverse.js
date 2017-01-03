
// Sets a default string for string reverse field on page load
var stringToReverseInput = document.getElementById("string-to-reverse");
var defaultString = "Example string";
stringToReverseInput.value = defaultString;

var btn = document.getElementById("button--reverse-string");

// Event listener for 'reverse' button, updates the output div with result from reverseString function
// with the input value passed
btn.addEventListener("click", function(){
	updateOutput(reverseString(stringToReverseInput.value));
});
 
/*
 ********************************************************************
 ************************CHALLENGE ANSWER ***************************
 ********************************************************************/
function reverseString(stringToReverse) {
	var reversedString = "";
 	for(var i = stringToReverse.length - 1; i >= 0; i--){
 		reversedString += stringToReverse.charAt(i);
 	}
 	return reversedString;
}

/********************************************************************
*********************************************************************
*********************************************************************/


// Update output div with passed reverse string
function updateOutput(reversedString) {
 	document.getElementById("output").innerHTML = reversedString;
}