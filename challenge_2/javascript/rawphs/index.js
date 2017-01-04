const testArray1 = [2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7]
const testArray2 = [2, 'a', 'l', 3, 'l',4,'k', 2, 3, 4, 'a', 6, 'c', 4, 'm', 6, 'm', 'k', 9, 10, 9, 8, 7, 8, 10, 7]

function findUnique (array) {
	return array.filter(
		item => array.indexOf(item) === array.lastIndexOf(item)
	)[0]
}

console.log(findUnique(testArray1))
console.log(findUnique(testArray2))

if (process.argv[2]) console.log(findUnique(JSON.parse(process.argv[2])))
