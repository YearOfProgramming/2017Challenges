package c12

import (
	"fmt"
	"strconv"
	"strings"
)

const MaxRunLength = 0xFFFF

func isAToZ(ch rune) bool {
	return ('a' <= ch && 'z' >= ch) || ('A' <= ch && 'Z' >= ch)
}

// Run Length Encodes the given string, compressing runs of single characters
// into the form c#1, where c is the character and 1 is the appropriate count.
// This only supports encoding strings which contain the character set
// [a-zA-Z]. No other characters are allowed. Character runs exceeding a 65535
// length will be split into 65535 length encodings.
func Encode(s string) (string, error) {
	ss := []string{}
	c := 0
	cch := '\x00'
	for _, ch := range s {
		if !isAToZ(ch) {
			return "", fmt.Errorf("Non-alphabetic character encountered: %c", ch)
		}
		large_count := false
		if cch == ch {
			c++
			if c < MaxRunLength {
				continue
			}
			large_count = true
		}
		if c > 1 {
			ss = append(ss, fmt.Sprintf("%c#%d", cch, c))
		} else if c == 1 {
			ss = append(ss, string(cch))
		}
		cch = ch
		c = 1
		if large_count {
			c = 0
		}
	}
	if c > 1 {
		ss = append(ss, fmt.Sprintf("%c#%d", cch, c))
	} else if c == 1 {
		ss = append(ss, string(cch))
	}
	return strings.Join(ss, ""), nil
}

func is0To9(ch rune) bool {
	return '0' <= ch && '9' >= ch
}

// Returns parsed count, new index, error value
func parseRepeatCount(rs []rune, i int) (idx, count int, err error) {
	idx = i
	mark := idx
	for idx < len(rs) && is0To9(rs[idx]) {
		idx++
	}
	if mark == idx {
		if idx >= len(rs) {
			err = fmt.Errorf("No repeat count specified")
		} else {
			err = fmt.Errorf("Non-digit character encountered for repeat count: %c", rs[idx])
		}
		return
	}
	c64, err := strconv.ParseInt(string(rs[mark:idx]), 10, 64)
	if err != nil {
		return
	}
	if c64 > MaxRunLength {
		err = fmt.Errorf("Excessive repeat count: %v", c64)
		return
	}
	count = int(c64)
	return
}

// rs is in/out
func appendRuneNTimes(rs *[]rune, ch rune, n int) {
	rout := *rs
	if cap(rout) < len(rout)+n {
		// Make the length identical to the current length to leverage copy().
		tmp := make([]rune, len(rout), cap(rout)*2+n)
		copy(tmp, rout)
		rout = tmp
	}
	for n > 0 {
		rout = append(rout, ch)
		n--
	}
	*rs = rout
}

// Expands the given Run Length Encoded string to its original value.
// Compressed runs of a single character are represented in the form c#1, where
// c is the character and 1 is the appropriate count. This only supports
// decoding strings which contain the character set [a-zA-Z]. No other
// characters are allowed. A maximum count of 65535 for a given character is
// allowed.
func Decode(s string) (string, error) {
	rs := []rune(s)
	rout := make([]rune, 0, len(rs)*2)
	for i := 0; i < len(rs); i++ {
		ch := rs[i]
		if !isAToZ(ch) {
			return "", fmt.Errorf("Non-alphabetic character encountered: %c", ch)
		}
		if i+1 >= len(rs) || rs[i+1] != '#' {
			rout = append(rout, ch)
			continue
		}
		iTmp, c, err := parseRepeatCount(rs, i+2)
		if err != nil {
			return "", err
		}
		// Rewind one character to counter the numeric character search.
		i = iTmp - 1
		appendRuneNTimes(&rout, ch, c)
	}
	return string(rout), nil
}
