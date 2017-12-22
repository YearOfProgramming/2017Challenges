# Single Number

###### Go 2

### 1. Solving the problem

My approach to solve this problem is to first find the single character
after each iteration and stop looking for further results.

This solution is very slow comparing to others,
but if performance is not a requirement,
this can be useful, because it has zero allocation in memory.

### 2. How to use and run this code

First you have to import this package into your main program:

```go
package main

import (
        "log"

        rchicoli "github.com/rchicoli/2017-challenges/challenge_2/go/rchicoli/src"
)

func main() {
        if single, err := rchicoli.SingleChar([]interface{}{2, 3, 2, 3, 6, 8, 2, 7, 9, 9, 7, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 5}); err == nil {
                log.Println("single character found: ", single)
        } else {
                log.Println(err)
        }
}
```

Then you can run it with:

```bash
$ go run main.go
```

For compile packages and dependencies, you have to type:

```bash
$ go build main.go
```

### 3. Testing

There are some tests set, to run them, use following command:

```bash
$ go test -v
=== RUN   TestSingleNumber
--- PASS: TestSingleNumber (0.00s)
=== RUN   TestSingleMixChar
--- PASS: TestSingleMixChar (0.00s)
=== RUN   TestSingleStrings
--- PASS: TestSingleStrings (0.00s)
PASS
ok      _/2017-challenges/challenge_2/go/rchicoli/src  0.001s
```
