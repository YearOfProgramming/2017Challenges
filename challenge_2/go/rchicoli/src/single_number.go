package rchicoli

import "errors"

// SingleChar returns a single character from a slice of interface
func SingleChar(x []interface{}) (interface{}, error) {
	var sliceSize = len(x)

OuterLoop:
	for i := 0; i < sliceSize; i++ {
		for j := 0; j < sliceSize; j++ {
			// do not compare same keys
			if i == j {
				// last record is single
				if j == sliceSize-1 {
					return x[i], nil
				}
				continue
			}
			// duplicate char found
			if x[i] == x[j] {
				continue OuterLoop
			}
			// end of slice and no match found
			// return single char
			if j == sliceSize-1 {
				return x[i], nil
			}
		}
	}
	return 0, errors.New("no single character found")

}
