package challenge6

import "fmt"

// Tracks the start and end points of a range of consecutive integers.
type Range struct {
	Start int
	End   int
}

// Creates a new range with Start and End equalling n.
func NewRange(n int) Range {
	return Range{Start: n, End: n}
}

func (r *Range) String() string {
	return fmt.Sprintf("%d->%d", r.Start, r.End)
}

type RangeSlice []Range

func (rs RangeSlice) ToStrings() []string {
	strs := make([]string, 0, len(rs))
	for _, r := range rs {
		strs = append(strs, r.String())
	}
	return strs
}

// Determines all ranges of consecutive values within the sorted input slice,
// ints. Resulting ranges consist of two or more values.
func FindRanges(ints []int) RangeSlice {
	if len(ints) <= 0 {
		return RangeSlice([]Range{})
	}
	ranges := make([]Range, 0, len(ints)/2)
	r := NewRange(ints[0])
	for _, i := range ints[1:] {
		if r.End+1 == i {
			r.End = i
		} else {
			if r.Start != r.End {
				ranges = append(ranges, r)
			}
			r = NewRange(i)
		}
	}
	if r.Start != r.End {
		ranges = append(ranges, r)
	}
	return RangeSlice(ranges)
}
