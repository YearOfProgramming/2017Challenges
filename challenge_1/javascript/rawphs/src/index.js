function reverseString (string) {
	return string.split('').reverse().join('')
}

console.log(reverseString(process.argv[2]))
