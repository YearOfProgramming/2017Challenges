document.getElementById('submit-string').addEventListener('click', function(e){
    var userStringInput = document.getElementById('user-string');
    var userStringValue = userStringInput.value;
    
    if(userStringValue){    
        initProblemSpecs(userStringValue);
        userStringValue = '';
    }
    e.preventDefault();
});

String.prototype.shuffle = function(){
	// Split the string into array
	var stringArray = this.split('');
	var stringLength = stringArray.length;

    
	for(var i = stringLength - 1; i > 0; i--) {
		var j = Math.floor(Math.random() * (i + 1));
		var temp = stringArray[i];
		stringArray[i] = stringArray[j];
		stringArray[j] = temp;
	}

	return stringArray.join('');

}

function initProblemSpecs(string) {
    var modifiedShuffledString = addLowerCaseLetter(string).shuffle();
    findDiff(string, modifiedShuffledString);
    
}

function addLowerCaseLetter(string){
    return string += 'e';
}

function findDiff(originalString, alteredString) {
	// loop through original string, removing characters from altered string
	for(var i = 0; i < originalString.length; i++){
		alteredString = alteredString.replace(originalString.charAt(i), '');
		console.log(alteredString);
	}
}


