package main

import (
	"fmt"
	"strings"
)

func reverseString(stringToReverse string) string {
  // limitations:  only works for strings, not UTF-8
  data := []string{}
  for i := 0; i < len(stringToReverse); i++ {
    data = append([]string{string(stringToReverse[i])}, data...)
  }

  return strings.Join(data, "")
}

func main() {
  var stringToReverse string = "easy as abc"
  fmt.Println(stringToReverse)
  fmt.Println(reverseString(stringToReverse))
}
