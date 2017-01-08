package natdm

import (
	"testing"
	"time"
)

var tr = &tree{
	A: &tree{
		A: &tree{
			V: 4,
		},
		B: &tree{
			V: 2,
			A: &tree{
				V: 100,
				A: &tree{
					V: 94,
				}, B: &tree{
					V: 66,
				},
			},
			B: &tree{},
		},
		V: 10,
	},
	B: &tree{
		A: &tree{
			V: 12,
		},
		B: &tree{
			V: 5,
		},
		V: 90,
	},
	V: 9,
}

func TestTreeSuccess(t *testing.T) {
	if err := reverse(tr, time.Second*2); err != nil {
		t.Error("expected no error, got " + err.Error())
		t.Fail()
	}
}

func TestTreeTimeout(t *testing.T) {
	if err := reverse(tr, 10); err == nil {
		t.Error("expected an error but got none")
		t.Fail()
	}
}
