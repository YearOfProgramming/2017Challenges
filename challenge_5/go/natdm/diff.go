package natdm

func diff(a, b string) (s string) {

	for _, x := range []byte(b) {
		for i, y := range []byte(a) {
			if x == y {
				break
			}
			if i == len(a)-1 {
				s = string(x)
				return
			}
		}
	}
	return
}
