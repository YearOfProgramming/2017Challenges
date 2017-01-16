// Gets user sequence, then splits to array
document.getElementById('submit').addEventListener('click', function(e){

    var userArray = document.getElementById('user-array').value;    

    userArray = userArray.split(/[ ,]+/g).filter(Boolean);

    printMissingNumber(findMissing(userArray));

    e.preventDefault();
    
});
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
// Compares the expected sum of the values in the userArray to the actual sum.
// The missing number will be the difference of the 2 sums.
function findMissing(userArray) {
    
    var userArrayExpectedSum = (userArray.length * (userArray.length + 1)) / 2;
    var userArrayActualSum =0;

    for(var i = 0; i < userArray.length; i++){
        // Parses elements to integers to perform sum
        userArrayActualSum += parseInt(userArray[i]);

    }

    return userArrayExpectedSum - userArrayActualSum;

}
//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------
function printMissingNumber(num) {

    document.getElementById('output').innerHTML = 
        '<p><b>Missing number is: </b>' + num + '</p>';

}