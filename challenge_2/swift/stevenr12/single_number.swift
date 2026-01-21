var array : [Int] = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
var counts : [Int:Int] = [:]
for value in array{
    counts[value] = (counts[value] ?? 0) + 1
}
print(counts.filter{$0.value == 1}[0].key)