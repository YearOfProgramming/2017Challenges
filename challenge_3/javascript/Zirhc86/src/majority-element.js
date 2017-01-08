var array = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7];

// Finds majority element using the Boyer-Moore majority vote algorithm which finds
// a majority candidate by increasing count each time currentMajority matches the current
// value, or by decreasing count if the values do not match. If count reaches 0, currentMajority
// is set to the next value in the array. Providing a majority exists, it will be the final value
// in currentMajority, as it would have had more increases than decreases. 
function findMajority(arr){
	var count = 0, currentMajority;

	for(var i = 0; i<arr.length; i++){
		if(count == 0){
			currentMajority = arr[i];
			count = 1;			
		}

		if(arr[i] == currentMajority){
			count++;
		}
		else{
			count--;
		}
	}

	// Here we check the number of occurences of the currentMajority candidate
	// to ensure a > 50% occurence
	count = 0;

	for(var i = 0; i<arr.length; i++){
		if(arr[i] == currentMajority){
			count++;
		}
	}

	return count > arr.length / 2 ? "Majority is: " + currentMajority : "No majority";
}

// For testing. Uses default array if none is passed by user
function test(arr){
	if(!arr){
		console.log("Testing with default array: " + array);
		arr = array;
	}

	console.log(findMajority(arr));
}

test();
