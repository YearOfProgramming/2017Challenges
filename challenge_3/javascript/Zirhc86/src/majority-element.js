var array = [2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7];

// Finds majority element using the Boyer-Moore majority vote algorithm.
function findMajority(arr){
	var count = 0, currentMajority;

	for(var i =0; i<arr.length; i++){
		if(count ==0){
			currentMajority = arr[i];
			count=1;			
		}

		if(arr[i] == currentMajority){
			count++;
		}
		else{
			count--;
		}
	}

	count=0;

	for(var i =0; i<arr.length; i++){
		if(arr[i] == currentMajority){
			count++;
		}
	}

	return count > arr.length/2 ? "Majority is: " + currentMajority : "No majority";
}


function test(arr){
	if(!arr){
		console.log("Testing with default array: " + array);
		arr = array;
	}

	console.log(findMajority(arr));
}

test();