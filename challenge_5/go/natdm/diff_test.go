package natdm

import "testing"

func TestDiff(t *testing.T) {
	if diff("1azfdafd4", "1azfdatfd4") != "t" {
		t.Error("expected t")
		t.Fail()
	}
}
