package natdm

func single(n []int) (i int) {
	m := make(map[int]int)

	for _, v := range n {
		m[v]++
	}
	for k, v := range m {
		if v == 1 {
			i = k
			break
		}
	}
	return
}
