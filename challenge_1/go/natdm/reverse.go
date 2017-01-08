package natdm

func reverse(s string) string {
	r := make([]byte, len(s))
	for i := range []byte(s) {
		r[i] = s[(len(s)-1)-i]
	}
	return string(r)
}
