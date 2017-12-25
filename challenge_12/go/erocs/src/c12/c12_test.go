package c12

import "testing"

func CheckGood(t *testing.T, raw, expect string) {
	s, err := Encode(raw)
	if err != nil {
		t.Error("Error encoding:", err)
	} else if s != expect {
		t.Error("Bad encoding:", s, "Expected:", expect)
	}
	s, err = Decode(s)
	if err != nil {
		t.Error("Error decoding:", err)
	} else if s != raw {
		t.Error("Bad decoding:", s, "Expected:", raw)
	}
}

func TestEmpty(t *testing.T) {
	CheckGood(t, "", "")
}

func TestSingleChar(t *testing.T) {
	CheckGood(t, "a", "a")
}

func TestMultiSameChar(t *testing.T) {
	CheckGood(t, "aaaaaaaaaaaa", "a#12")
}

func TestMultipleSingles(t *testing.T) {
	CheckGood(t, "abcdefgh", "abcdefgh")
}

func TestMultipleMultiples(t *testing.T) {
	CheckGood(t, "aaabbbaaacccaaaaaaaaaaaadddddddddddddddddd", "a#3b#3a#3c#3a#12d#18")
}

func TestMixed1(t *testing.T) {
	CheckGood(t, "aaabaaacaaadaaaeaaa", "a#3ba#3ca#3da#3ea#3")
}

func TestMixed2(t *testing.T) {
	CheckGood(t, "abbbacccaddda", "ab#3ac#3ad#3a")
}

func TestMixed3(t *testing.T) {
	CheckGood(t, "aaab", "a#3b")
}

func TestMixed4(t *testing.T) {
	CheckGood(t, "abbb", "ab#3")
}

func TestUppercase(t *testing.T) {
	CheckGood(t, "AaBBbbcCddDD", "AaB#2b#2cCd#2D#2")
}

func TestReallyLongRune(t *testing.T) {
	ll := 0x10011
	rs := make([]rune, 0, ll)
	for i := 0; i < ll; i++ {
		rs = append(rs, 'a')
	}
	s := string(rs)
	CheckGood(t, s, "a#65535a#18")
}

func TestBadChar1(t *testing.T) {
	_, err := Encode("@")
	if err == nil {
		t.Fail()
	}
}

func TestBadChar2(t *testing.T) {
	_, err := Encode("[")
	if err == nil {
		t.Fail()
	}
}

func TestBadChar3(t *testing.T) {
	_, err := Encode("{")
	if err == nil {
		t.Fail()
	}
}

func TestBadDecoding1(t *testing.T) {
	_, err := Decode("a#")
	if err == nil {
		t.Fail()
	}
}

func TestBadDecoding2(t *testing.T) {
	_, err := Decode("a#a")
	if err == nil {
		t.Fail()
	}
}

func TestBadDecoding3(t *testing.T) {
	_, err := Decode("a#99999")
	if err == nil {
		t.Fail()
	}
}

func TestBadDecoding4(t *testing.T) {
	_, err := Decode("a#9999999999999999999999999999999999999999999")
	if err == nil {
		t.Fail()
	}
}
