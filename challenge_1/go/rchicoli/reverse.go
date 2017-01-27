package rchicoli

// ReverseString reverses a string
func ReverseString(s string) string {
	unicodeString := []int32(s)
	l := len(unicodeString)
	r := make([]int32, l)
	l--
	for k, v := range unicodeString {
		r[l-k] = v
	}
	return string(r)
}
