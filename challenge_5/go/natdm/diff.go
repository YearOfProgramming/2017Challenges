package natdm

import "math/rand"

// shuffleAndAdd shuffles and adds one character at random
func shuffleAndAdd(s string) (b byte, out []byte) {
	// Get a new letter
	alp := []byte("abcdefghijklmnopqrstuvwxyz")
	b = alp[rand.Intn(len(alp))]

	// Add it to a new slice that contains the base string/bytes
	orig := append([]byte(s), b)
	// Establish return slice
	out = make([]byte, len(orig))

	// Keep track of indexes already used to pluck a random byte from
	pickedIndexes := []int{}

	for i := 0; i < len(orig); i++ {
	draw:
		r := rand.Intn(len(orig))
		for _, v := range pickedIndexes {
			if v == r {
				goto draw
			}
		}
		pickedIndexes = append(pickedIndexes, r)
		out[i] = orig[r]
	}
	return
}

func diff(a, b string) (s string) {
	var orig []byte
	var n []byte
	if a > b {
		n = append(n, []byte(a)...)
		orig = append(orig, []byte(b)...)
	} else {
		n = append(n, []byte(b)...)
		orig = append(orig, []byte(a)...)
	}

	chars := make(map[byte]int)
	for _, v := range orig {
		chars[v]++
	}

	for _, v := range n {
		if c, ok := chars[v]; ok && c > 0 {
			chars[v]--
		} else {
			s = string(v)
			return
		}
	}
	return
}
