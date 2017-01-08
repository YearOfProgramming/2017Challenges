package natdm

import "testing"

func TestMajority(t *testing.T) {
	m := majority([]int{2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 7, 7, 7, 7, 7, 7, 7, 7, 7, 10})
	if m != 7 {
		t.Error("expected 7")
		t.Fail()
	}
}
