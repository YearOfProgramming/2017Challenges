// max_occurance_test
package main

import (
	"testing"
)

func TestIntegers(t *testing.T) {
	input := []interface{}{2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6}
	output := 4
	result := FindMajority(input)
	if result != output {
		t.Error("for", input,
			"expected", output,
			"got", result)
	}
}

func TestStrings(t *testing.T) {
	input := []interface{}{"a", "a", "b", "b", "b", "b", "c", "c", "c", "c",
		"c", "d", "d", "e"}
	output := "c"
	result := FindMajority(input)
	if result != output {
		t.Error("for", input,
			"expected", output,
			"got", result)
	}
}

func TestMultipleTypes(t *testing.T) {
	input := []interface{}{2, "a", "l", 3, "l", 4, "k", 2, 3, 4, "a", 6, "c",
		4, "m", 6, "m", "k", 9, 10, 9, 8, 7, 8, 10, 7, 7, 7, 7, 7, 7, 7, 7, 7}
	output := 7
	result := FindMajority(input)
	if result != output {
		t.Error("for", input,
			"expected", output,
			"got", result)
	}
}
