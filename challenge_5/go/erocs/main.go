package main

import (
	"challenge5"
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Fprintln(os.Stderr, "Please provide two strings to test.")
		os.Exit(1)
	}
	ch, err := challenge5.FindExtraLetter(os.Args[1], os.Args[2])
	if err != nil {
		fmt.Fprintln(os.Stderr, "Error:", err.Error())
		os.Exit(2)
	}
	fmt.Println("Found character:", ch)
}
