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
