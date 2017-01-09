

document.getElementById('submit').addEventListener('click', function(e){
    var userArray = document.getElementById('user-array').value;
    var lowerRange = [];
    var upperRange = [];
    var userArrayRanges = [];

    // Separate user string into an array, removing any
    // spaces and/or commas
    userArray = userArray.split(/[ ,]+/g).filter(Boolean);
    
    // Sort lower and upper ranges by comparing previous
    // element to current element. If the difference of
    // the current element from the previous element is not
    // 1, the previous element becomes the next entry for
    // upperRange[] and the current element becomes a new
    // element for lowerRange[]. The last element is always
    // a new element in upperRange[].
    lowerRange.push(userArray[0]);

    for(var i = 1; i < userArray.length; i++) {

        if(userArray[i] - userArray[i-1] != 1){

            upperRange.push(userArray[i-1]);

            lowerRange.push(userArray[i]);
        }
        if(i == userArray.length - 1){

            upperRange.push(userArray[i]);
        }
    }

    userArrayRanges = setRanges(lowerRange, upperRange);

    printRanges(userArrayRanges);

    e.preventDefault();
	
});
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
// Compare indexed elements between lower and upper range
// arrays. If the 2 values are the same, no new range is
// added to ranges[].
function setRanges(lowerRange, upperRange) {
	
    var ranges = [];

    if(lowerRange.length < 1){

        return ranges;		
    }

    for( var i = 0; i < lowerRange.length; i++) {

        if(upperRange[i] > lowerRange[i]) {

            ranges.push(lowerRange[i] + " -> " + upperRange[i]);
        }
    }
	
    return ranges;
}
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
function printRanges(ranges) {

    if(ranges.length > 0){

        document.getElementById('output').innerHTML = '<b>Ranges:</b>';		
    }
    else {

        document.getElementById('output').innerHTML = '<b>There are no ranges</b>';
    }

    for(var i = 0; i < ranges.length; i++) {

        document.getElementById('output').innerHTML += '<p>' + ranges[i] + '</p>';
    }
}
