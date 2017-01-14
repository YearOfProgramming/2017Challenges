// Take an array of mixed data types and find the element that occurs
// only once in it.
package main

import (
	"fmt"
)

// Finds the single occurance, takes in interface as input and output params
//as elements in the given array may be of any data type
func FindSingle(input []interface{}) (result interface{}) {
	// Create a hashmap, where element of that array is key and its number of
	// occurances is the value.
	occurances := make(map[interface{}]int)
	for _, key := range input {
		occurances[key]++
	}
	// Return when we find the single occurance.
	for k, v := range occurances {
		if v == 1 {
			result = k
			break
		}
	}
	return result
}

func main() {
	given := []interface{}{2, "a", "l", 3, "l", 4, "k", 2, 3, 4, "a", 6, "c",
		4, "m", 6, "m", "k", 9, 10, 9, 8, 7, 8, 10, 7}
	fmt.Printf("Given array is : %v \n", given)
	result := FindSingle(given)
	fmt.Printf("Element that occur only once : %v \n", result)
}
