package main

import "testing"

func TestFindMajority(t *testing.T) {

	if output := findMajority([]int{2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7, 7, 7, 7}); output != 7 {
		t.Errorf("expected 7, got: %d\n", output)
	}

}
