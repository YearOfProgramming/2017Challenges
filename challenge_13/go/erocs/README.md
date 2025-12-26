# Challenge 13: Integer Palindrome

## 1. Solution Description

Divide the given value by 10 until it is 0 to extract all digits and store those into a slice. Then just check that each element of the first half of the slice is mirrored on the other half.

## 2. Running Tests

In bash in this directory:

    export GOPATH=`pwd`
    go test c13
