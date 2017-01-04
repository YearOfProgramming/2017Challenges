package main

import (
	"fmt"
)

func FindMajority(int_array []int) int {
	max_num := 0
	max_count := 0
	counter := make(map[int]int)
	for _, n := range int_array {
		if _, ok := counter[n]; ok {
			counter[n]++
		} else {
			counter[n] = 1
		}
		if counter[n] > max_count {
			max_num = n
			max_count = counter[n]
		}
	}
	return max_num
}

func main() {
	a := []int{2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7, 7, 7, 7}
	fmt.Printf("Majority element: %d\n", FindMajority(a))
}
