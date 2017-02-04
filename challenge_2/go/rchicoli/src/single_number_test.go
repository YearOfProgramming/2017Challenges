package rchicoli

import "testing"

func TestSingleNumber(t *testing.T) {
	expected := 5
	randomNumbers := []interface{}{2, 3, 2, 3, 6, 8, 2, 7, 9, 9, 7, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 5}
	if output, err := SingleChar(randomNumbers); err != nil || output != expected {
		t.Errorf("given array =\"%v\", %v\nreturn \"%v\" and expected \"%v\"", randomNumbers, err, output, expected)
	}
}

func TestSingleMixChar(t *testing.T) {
	expected := 5
	randomCharacters := []interface{}{2, 3, 5, 2, 3, 6, 8, 2, 7, "l", 9, 9, 7, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7}
	if output, err := SingleChar(randomCharacters); err != nil || output != expected {
		t.Errorf("given array =\"%v\", %v\nreturn \"%v\" and expected \"%v\"", randomCharacters, err, output, expected)
	}
}

func TestSingleStrings(t *testing.T) {
	expected := "e"
	randomStrings := []interface{}{"a", "b", "c", "d", "e", "f", "a", "b", "c", "d", "f"}
	if output, err := SingleChar(randomStrings); err != nil || output != expected {
		t.Errorf("given array =\"%v\", %v\nreturn \"%v\" and expected \"%v\"", randomStrings, err, output, expected)
	}
}
