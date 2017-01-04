const testArray = [
	2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

function findMajority (array) {
	let majority = Math.floor(array.length/2)
	let count    = {}

	array.forEach(item => count[item] ? count[item] += 1 : count[item] = 1)

	return Object.keys(count).filter(item => count[item] > majority)[0]
}

console.log(findMajority(testArray))

if (process.argv[2]) console.log(findMajority(JSON.parse(process.argv[2])))
