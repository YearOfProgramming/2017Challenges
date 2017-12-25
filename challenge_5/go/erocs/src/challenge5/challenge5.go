package challenge5

import "fmt"

func FindExtraLetter(s, t string) (string, error) {
	letters := make(map[rune]int)
	for _, ch := range t {
		if _, ok := letters[ch]; ok {
			letters[ch]++
		} else {
			letters[ch] = 1
		}
	}
	for _, ch := range s {
		if _, ok := letters[ch]; ok {
			letters[ch]--
			if letters[ch] <= 0 {
				delete(letters, ch)
			}
		} else {
			return "", fmt.Errorf("Letter '%c' in source is not in target.", ch)
		}
	}
	const nul rune = 0x0
	letter := nul
	for ch, _ := range letters {
		if letter != nul {
			return "", fmt.Errorf("Letter '%c' in target is a second extra. The first was '%c'.", ch, letter)
		}
		letter = ch
	}
	if letter == nul {
		return "", fmt.Errorf("No difference found.")
	}
	if letters[letter] != 1 {
		return "", fmt.Errorf("Target contains multiple letter '%c'. Count: %d", letter, letters[letter])
	}
	return string(letter), nil
}
