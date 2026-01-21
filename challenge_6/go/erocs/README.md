# Challenge 6: Determine Ranges

## 1. Solution Description

Since the input slice will always be sorted, this code creates a new _Range_
using the first number. Subsequent numbers that are a single integer larger then
the previous will update the _Range_'s End value to match. When the end of the
input slice or a non-consecutive value is encountered, the current _Range_ will
be appended to the result slice and a new _Range_ will be created using the
value. Single value _Range_s (ex. 1->1) are omitted from the result slice.

## 2. Running Tests

In bash in this directory:

    export GOPATH=`pwd`
    go test challenge6
