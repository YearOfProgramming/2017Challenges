package main

import (
	"fmt"
)

func ReverseString(s string) string {
	l := len(s)
	r := make([]rune, l)
	l--
	for i, ch := range s {
		r[l-i] = ch
	}
	return string(r)
}

func main() {
	orig := "hello"
	fmt.Printf("%s reversed is %s\n", orig, ReverseString(orig))
}
