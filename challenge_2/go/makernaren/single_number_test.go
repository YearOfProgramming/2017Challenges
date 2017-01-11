// single_number_test
package main

import (
	"testing"
)

func TestIntegers(t *testing.T) {
	input := []interface{}{2, 2, 3, 3, 4, 4, 5, 5, 6}
	output := 6
	result := FindSingle(input)
	if result != output {
		t.Error("for", input,
			"expected", output,
			"got", result)
	}
}

func TestStrings(t *testing.T) {
	input := []interface{}{"a", "a", "b", "b", "c", "c", "d", "d", "e"}
	output := "e"
	result := FindSingle(input)
	if result != output {
		t.Error("for", input,
			"expected", output,
			"got", result)
	}
}

func TestMultipleTypes(t *testing.T) {
	input := []interface{}{2, "a", "l", 3, "l", 4, "k", 2, 3, 4, "a", 6, "c",
		4, "m", 6, "m", "k", 9, 10, 9, 8, 7, 8, 10, 7}
	output := "c"
	result := FindSingle(input)
	if result != output {
		t.Error("for", input,
			"expected", output,
			"got", result)
	}
}
