package c13

func splitDigits(n uint64, base uint64) []byte {
	out := make([]byte, 0, 22) // 22 is max length base-8 represented 64-bit value
	for n > 0 {
		r := n % base
		n = n / base
		out = append(out, byte(r))
	}
	return out
}

func IsPalindrome64(n uint64) bool {
	ds := splitDigits(n, 10)
	ll := len(ds)
	hl := ll / 2
	ll--
	for i := 0; i < hl; i++ {
		if ds[i] != ds[ll-i] {
			return false
		}
	}
	return true
}
