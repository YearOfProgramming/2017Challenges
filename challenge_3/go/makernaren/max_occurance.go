// Take an array of mixed data types and find the element that occurs
// most number of times.
package main

import (
	"fmt"
)

// Finds the maximum occurance, takes in interface as input and output params
//as elements in the given array may be of any data type
func FindMajority(input []interface{}) (result interface{}) {
	// Create a hashmap, where element of that array is key and its number of
	// occurances is the value.
	occurances := make(map[interface{}]int)
	for _, key := range input {
		occurances[key]++
	}
	// Return when we find the max occurance.
	max := 0
	kv_pair := make([]interface{}, 2)
	for k, v := range occurances {
		// Replace the variable until you find max
		if v > max {
			max = v
			kv_pair[0] = k
			kv_pair[1] = v
		}
	}
	return kv_pair[0]
}

func main() {
	given := []interface{}{2, "a", "l", 3, "l", 4, "k", 2, 3, 4, "a", 6, "c",
		4, "m", 6, "m", "k", 9, 10, 9, 8, 7, 8, 10, 7}
	fmt.Printf("Given array is : %v \n", given)
	result := FindMajority(given)
	fmt.Printf("Element that occur only max number of times : %v \n", result)
}
