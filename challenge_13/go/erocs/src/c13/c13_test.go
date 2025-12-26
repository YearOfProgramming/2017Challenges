package c13

import (
	"testing"
)

func CheckGood(t *testing.T, n uint64) {
	if !IsPalindrome64(n) {
		t.Fail()
	}
}

func CheckBad(t *testing.T, n uint64) {
	if IsPalindrome64(n) {
		t.Fail()
	}
}

func TestGL1(t *testing.T) {
	CheckGood(t, 1)
}

func TestGL2(t *testing.T) {
	CheckGood(t, 11)
}

func TestGL3(t *testing.T) {
	CheckGood(t, 121)
}

func TestGL4(t *testing.T) {
	CheckGood(t, 1221)
}

func TestBL2(t *testing.T) {
	CheckBad(t, 12)
}

func TestBL3(t *testing.T) {
	CheckBad(t, 112)
}

func TestBL4(t *testing.T) {
	CheckBad(t, 1112)
	CheckBad(t, 1121)
}

func TestGMax(t *testing.T) {
	CheckGood(t, 11111111111111111111)
}

func TestBMax(t *testing.T) {
	CheckBad(t, 11111111111111111112)
	CheckBad(t, 11111111112111111111)
}
