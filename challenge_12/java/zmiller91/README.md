# Compression and Decompression

This solution compresses and decompresses a string of alphabetic characters
by turning a repeating sequence into `character#repeated`, assuming the sequence
is repeated more than 3 times. 

## How To Run

```
javac Compression.java
java Compression
```

## Discussion

* Space: O(N)
* Time: O(N)

The solution builds a new string as it's compressed; if that space isn't  
considered in the space complexity, then the solution would use O(1) space. This
solution works with empty strings and builds the compressed and decompressed
strings with a single pass.