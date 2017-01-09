package main

import (
	"fmt"
)

func Reverse(to_reverse string) string {
	// Create a rune slice from the string, Reverse that slice
	runed := []rune(to_reverse)
	for i, j := 0, len(runed)-1; i < j; i, j = i+1, j-1 {
		runed[i], runed[j] = runed[j], runed[i]
	}
	return string(runed)
}

func main() {
	input := "hello"
	fmt.Println("Input string : ", input)
	reversed := Reverse(input)
	fmt.Println("Reversed string : ", reversed)
}
