package natdm

import "testing"

func TestDiff(t *testing.T) {
	word := "1asafsd23"
	randByte, newBytes := shuffleAndAdd(word)
	randChar := string(randByte)
	newWord := string(newBytes)
	foundChar := diff(word, newWord)

	if foundChar != randChar {
		t.Errorf("expected %s", string(randChar))
		t.Fail()
	}
}

func TestDiffDupe(t *testing.T) {
	word := "1asafsd23"
	newWord := "1asaafsd23"

	foundChar := diff(word, newWord)

	if foundChar != "a" {
		t.Errorf("expected %s but got %s", "a", foundChar)
		t.Fail()
	}
}
