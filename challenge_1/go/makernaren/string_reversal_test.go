package main

import (
	"testing"
)

func TestString(t *testing.T) {
	test_cases := map[string]string{
		"hello":         "olleh",
		"I love Golang": "gnaloG evol I",
		"Bond007":       "700dnoB",
	}
	for input, expected := range test_cases {
		reversed := Reverse(input)
		if reversed != expected {
			t.Error("for", input,
				"expected", expected,
				"got", reversed)
		}
	}
}
