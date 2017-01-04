package natdm

import (
	"log"
	"testing"
)

func TestDiff(t *testing.T) {
	w := "1asafsd23"
	x, n := shuffleAndAdd(w)
	log.Println(w)
	log.Println(string(x))
	log.Println(string(n))
	if diff(w, string(n)) != string(x) {
		t.Errorf("expected %s", string(x))
		t.Fail()
	}
}
