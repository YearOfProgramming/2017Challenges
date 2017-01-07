package natdm

func majority(n []int) (i int) {
	m := make(map[int]int)

	for _, v := range n {
		m[v]++
	}

	for k, v := range m {
		if v > m[i] {
			i = k
		}
	}
	return
}
