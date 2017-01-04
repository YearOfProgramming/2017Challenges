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
	ob, nb := []byte{}, []byte{}
	orig, big := make(map[byte]int), make(map[byte]int)

	if a > b {
		ob = append(ob, []byte(b)...)
		nb = append(nb, []byte(a)...)
	} else {
		ob = append(ob, []byte(a)...)
		nb = append(nb, []byte(b)...)
	}

	for _, v := range nb {
		big[v]++
	}

	for _, v := range ob {
		orig[v]++
	}

	for k, v := range big {
		if orig[k] != v {
			s = string(k)
			break
		}
	}
	return
}
