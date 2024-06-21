package challenge6

import (
	"strings"
	"testing"
)

// Call challenge6.FindRanges() on _ints_ and concatenate the ranges into a
// single string for comparison testing.
func FR(ints []int) string {
	return strings.Join(FindRanges(ints).ToStrings(), " ")
}

func TestEmpty(t *testing.T) {
	ex := ""
	r := FR([]int{})
	if r != ex {
		t.Error("Mismatch, expected:", ex, "received:", r)
	}
}

func TestSingleton(t *testing.T) {
	ex := ""
	r := FR([]int{1})
	if r != ex {
		t.Error("Mismatch, expected:", ex, "received:", r)
	}
}

func TestSimpleRange(t *testing.T) {
	ex := "1->2"
	r := FR([]int{1, 2})
	if r != ex {
		t.Error("Mismatch, expected:", ex, "received:", r)
	}
}

func TestNegativeRange(t *testing.T) {
	ex := "-2->-1"
	r := FR([]int{-2, -1})
	if r != ex {
		t.Error("Mismatch, expected:", ex, "received:", r)
	}
}

func TestLongRange(t *testing.T) {
	ex := "1->20000"
	c := 20000
	ints := make([]int, 0, c)
	for i := 1; i <= c; i++ {
		ints = append(ints, i)
	}
	r := FR(ints)
	if r != ex {
		t.Error("Mismatch, expected:", ex, "received:", r)
	}
}

// TestTwoRanges
func TestRR(t *testing.T) {
	ex := "10->12 14->16"
	r := FR([]int{10, 11, 12, 14, 15, 16})
	if r != ex {
		t.Error("Mismatch, expected:", ex, "received:", r)
	}
}

// TestSingletonRangeSingleton
func TestSRS(t *testing.T) {
	ex := "4->6"
	r := FR([]int{2, 4, 5, 6, 8})
	if r != ex {
		t.Error("Mismatch, expected:", ex, "received:", r)
	}
}

// TestRangeSingletonRange
func TestRSR(t *testing.T) {
	ex := "1->3 7->9"
	r := FR([]int{1, 2, 3, 5, 7, 8, 9})
	if r != ex {
		t.Error("Mismatch, expected:", ex, "received:", r)
	}
}
