package challenge10

import (
	"testing"
)

func TestNoClosers(t *testing.T) {
	if !HasValidClosers("The quack brown fax jumped over the dazy dog.") {
		t.Fail()
	}
}

func TestSingleCloser(t *testing.T) {
	if !HasValidClosers("(Y)") {
		t.Fail()
	}
}

func TestNoOpener(t *testing.T) {
	if HasValidClosers("hi)") {
		t.Fail()
	}
}

func TestNoCloser(t *testing.T) {
	if HasValidClosers("(hi") {
		t.Fail()
	}
}

func TestParens(t *testing.T) {
	if !HasValidClosers("()") {
		t.Error("Bad valid order")
	}
	if HasValidClosers(")(") {
		t.Error("Bad invalid order")
	}
}

func TestBrackets(t *testing.T) {
	if !HasValidClosers("[]") {
		t.Error("Bad valid order")
	}
	if HasValidClosers("][") {
		t.Error("Bad invalid order")
	}
}

func TestBraces(t *testing.T) {
	if !HasValidClosers("{}") {
		t.Error("Bad valid order")
	}
	if HasValidClosers("}{") {
		t.Error("Bad invalid order")
	}
}

func TestLtGt(t *testing.T) {
	if !HasValidClosers("<>") {
		t.Error("Bad valid order")
	}
	if HasValidClosers("><") {
		t.Error("Bad invalid order")
	}
}

func TestValidNesting(t *testing.T) {
	if !HasValidClosers("{[(<>)[<<{}>>]]}") {
		t.Fail()
	}
}

func TestInvalidNesting(t *testing.T) {
	if HasValidClosers("({[<)}]>") {
		t.Fail()
	}
}

func TestDeepNesting(t *testing.T) {
	l := 20000
	rs := make([]rune, 0, l*2)
	for i := 1; i <= l; i++ {
		fizz := i%3 == 0
		buzz := i%5 == 0
		if fizz && buzz {
			rs = append(rs, '(')
		} else if fizz {
			rs = append(rs, '[')
		} else if buzz {
			rs = append(rs, '{')
		} else {
			rs = append(rs, '<')
		}
	}
	for i := l - 1; i >= 0; i-- {
		rs = append(rs, openers[rs[i]])
	}
	s := string(rs)
	if !HasValidClosers(s) {
		t.Fail()
	}
}
