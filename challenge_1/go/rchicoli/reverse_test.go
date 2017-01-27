package rchicoli

import "testing"

func TestReverse(t *testing.T) {
	expected := "héllö yöü"
	if output := ReverseString("üöy ölléh"); output != expected {
		t.Errorf("given str=\"%s\", return \"%s\"", expected, output)
	}
}
