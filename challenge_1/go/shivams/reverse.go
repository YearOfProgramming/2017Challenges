package main

import (
	"fmt"
	//"strings"
)

func reverseString(str string) string {
	var revStr string
	for i := len(str) - 1; i >= 0; i-- {
		revStr = revStr + string(str[i])
	}
	return revStr

}

func main() {
	var str string
	fmt.Println("Enter the string to reverse: ")
	fmt.Scanf("%s", &str)
	fmt.Println(reverseString(str))
}
