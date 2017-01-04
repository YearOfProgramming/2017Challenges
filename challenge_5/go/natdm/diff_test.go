package natdm

import "testing"

func TestDiff(t *testing.T) {
	w := "1asafsd23"
	x, n := shuffleAndAdd(w)
	if diff(w, string(n)) != string(x) {
		t.Errorf("expected %s", string(x))
		t.Fail()
	}
}
