document.getElementById('submit-string').addEventListener('click', function(e){
    
    var userString = document.getElementById('user-string').value;
    var userChar = document.getElementById('user-extra-char').value;
    
    var modifiedString = userString + userChar;
       
    initProblemSpecs(userString, modifiedString);
    
    e.preventDefault();
});

// --------------------------------------------------
// --------------------------------------------------

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
// ----------------------------------------------------
// ----------------------------------------------------
function initProblemSpecs(userString, modifiedString) {
    var modifiedShuffledString = modifiedString.shuffle();
    var addedChar = findDiff(userString, modifiedShuffledString);
    

    if(addedChar == ' ') {
        addedChar = 'space';
    }
    
    printResult(userString, modifiedShuffledString, addedChar);
    
}
// --------------------------------------------------
// --------------------------------------------------
function printResult(userString, modifiedShuffledString, addedChar) {
    var userStringNotice = "<b>The entered string was:</b> " + userString;
    var modifiedStringNotice = "<b>The modified string was:</b> " + modifiedShuffledString;
    var addedCharNotice = "<b>The added character is:</b> " + addedChar;
    
    var pTag = '<p>';
    var pTagClose = '</p>';
    document.getElementById('output').innerHTML = 
        pTag + userStringNotice + pTagClose +
        pTag + modifiedStringNotice + pTagClose +
        pTag + addedCharNotice + pTagClose; 

}
// --------------------------------------------------
// --------------------------------------------------

// Find the added char by removing each char of the original
// string from the modified string
function findDiff(originalString, modifiedString) {
    // loop through original string, removing characters from altered string
    for(var i = 0; i < originalString.length; i++){
        modifiedString = modifiedString.replace(originalString.charAt(i), '');
    }
    return modifiedString;
}

// --------------------------------------------------
// --------------------------------------------------