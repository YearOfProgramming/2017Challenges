package challenge5

import (
	"fmt"
	"math/rand"
	"strings"
	"testing"
	"time"
)

func NewRand(t *testing.T) *rand.Rand {
	seed := time.Now().UnixNano()
	t.Logf("Random seed: %d", seed)
	return rand.New(rand.NewSource(seed))
}

func RandomizeString(rnd *rand.Rand, s string) string {
	result := []rune(s)
	for i := len(result) - 1; i > 0; i-- {
		idx := rnd.Int31n(int32(i))
		tmp := result[i]
		result[i] = result[idx]
		result[idx] = tmp
	}
	return string(result)
}

func TestRandomizeString(t *testing.T) {
	rnd := NewRand(t)
	source := "abcd"
	result := RandomizeString(rnd, source)
	if source == result {
		t.Error("String not randomized.")
	} else if len(source) != len(result) {
		t.Error("Randomized string length differs from source length.")
	} else if !strings.ContainsRune(result, 'a') || !strings.ContainsRune(result, 'b') || !strings.ContainsRune(result, 'c') || !strings.ContainsRune(result, 'd') {
		t.Error("Randomized string has different characters from source.")
	}
}

var asciiLetters = []rune("abcdefghijklmnopqrstuvwxyz")

func RandomAsciiRune(rnd *rand.Rand) rune {
	idx := rnd.Int31n(int32(len(asciiLetters)))
	return asciiLetters[idx]
}

func NewRandomAsciiString(rnd *rand.Rand, length int) string {
	result := make([]rune, length)
	for i := 0; i < length; i++ {
		result[i] = RandomAsciiRune(rnd)
	}
	return string(result)
}

func ExpectValid(t *testing.T, source, tester, result string) {
	ch, err := FindExtraLetter(source, tester)
	if err != nil {
		t.Error(err)
	} else if ch != result {
		t.Errorf("Result was not %s: %s", result, ch)
	} else {
		t.Logf("Valid %s vs %s finds %s", source, tester, ch)
	}
}

func ExpectError(t *testing.T, source, tester, error_substring string) {
	_, err := FindExtraLetter(source, tester)
	if err == nil {
		t.Error("No error generated")
	} else if !strings.Contains(err.Error(), error_substring) {
		t.Error("Unexpected error:", err)
	}
}

func TestSimple(t *testing.T) {
	ExpectValid(t, "a", "ab", "b")
}

func Test10As(t *testing.T) {
	ExpectValid(t, "aaaaaaaaaa", "aaaaaaaaaaa", "a")
}

func Test10Randomized(t *testing.T) {
	rnd := NewRand(t)
	source := "abcdefghij"
	tester := RandomizeString(rnd, "abcdefghijk")
	ExpectValid(t, source, tester, "k")
}

func Test1000Randomized(t *testing.T) {
	rnd := NewRand(t)
	source := NewRandomAsciiString(rnd, 1000)
	expect := string(RandomAsciiRune(rnd))
	tester := RandomizeString(rnd, fmt.Sprintf("%s%s", source, expect))
	ExpectValid(t, source, tester, expect)
}

func TestEmptySource(t *testing.T) {
	ExpectValid(t, "", "a", "a")
}

func TestEmptyTester(t *testing.T) {
	ExpectError(t, "a", "", "in source is not in target")
}

func TestSimpleEqual(t *testing.T) {
	ExpectError(t, "aaa", "aaa", "No difference found.")
}

func TestSimpleMultipleExactExtras(t *testing.T) {
	ExpectError(t, "aaa", "aaabb", "Target contains multiple letter")
}

func TestSimpleMultipleDifferentExtras(t *testing.T) {
	ExpectError(t, "aaa", "aaabc", "in target is a second extra. The first was")
}

func Test10RandomizedEqual(t *testing.T) {
	rnd := NewRand(t)
	source := "abcdefghij"
	tester := RandomizeString(rnd, source)
	ExpectError(t, source, tester, "No difference found.")
}

func Test1000RandomizedEqual(t *testing.T) {
	rnd := NewRand(t)
	source := NewRandomAsciiString(rnd, 1000)
	tester := RandomizeString(rnd, source)
	ExpectError(t, source, tester, "No difference found.")
}
