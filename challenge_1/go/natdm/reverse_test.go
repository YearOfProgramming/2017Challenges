package natdm

import "testing"

func TestReverse(t *testing.T) {
	exp := "dlrow olleh"
	if actual := reverse("hello world"); actual != exp {
		t.Errorf("expected %s, got %s", exp, actual)
		t.Fail()
	}
}
