package main

import (
	"fmt"
)

func FindSingleton(int_array []int) (found int) {
	singles := make(map[int]int)
	repeats := make(map[int]int)
	for _, n := range int_array {
		if _, ok := repeats[n]; ok {
			repeats[n]++
		} else if _, ok := singles[n]; ok {
			delete(singles, n)
			repeats[n] = 2
		} else {
			singles[n] = 1
		}
	}
	for k, _ := range singles {
		found = k
	}
	return
}

func main() {
	a := []int{2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7}
	fmt.Printf("Singleton: %d\n", FindSingleton(a))
}
