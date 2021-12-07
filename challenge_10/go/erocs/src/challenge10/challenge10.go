package challenge10

import (
	lane "gopkg.in/oleiade/lane.v1"
)

var openers map[rune]rune = map[rune]rune{
	'(': ')',
	'[': ']',
	'{': '}',
	'<': '>',
}

var closers map[rune]rune

// Initialize package private variables.
func init() {
	closers = map[rune]rune{}
	for k, v := range openers {
		closers[v] = k
	}
}

func HasValidClosers(s string) bool {
	stk := lane.NewStack()
	for _, ch := range s {
		if closer, ok := openers[ch]; ok {
			stk.Push(closer)
		} else if !stk.Empty() && ch == stk.Head().(rune) {
			stk.Pop()
		} else if _, ok := closers[ch]; ok {
			// Closer without an opener
			return false
		}
	}
	return stk.Empty()
}
