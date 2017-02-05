package main

import "fmt"

func findMajority(n []int) int {
	m := make(map[int]int)
	l := make([]int, 1)

	for _, v := range n {
		m[v]++
	}

	for k, v := range m {
		if v > l[0] {
			l[0] = k
		}
	}
	return l[0]
}

func main() {

	fmt.Println(findMajority([]int{2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7, 7, 7, 7}))

}
