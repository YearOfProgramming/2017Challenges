package natdm

import "testing"

func TestSingle(t *testing.T) {
	if s := single([]int{2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7}); s != 5 {
		t.Errorf("expected 5 but got %v", s)
		t.Fail()
	}
}
