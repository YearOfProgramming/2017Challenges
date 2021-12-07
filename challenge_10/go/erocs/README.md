# Challenge 10: Match Closers

## 1. Solution Description

Create a pushdown atomata (utilizing a stack) to verify character group opening
characters are matched with appropriate closing characters in a given string.
Supported character sets:

    Opener  Closer
    (       )
    [       ]
    {       }
    <       >

## 2. Running Tests

In bash in this directory:

    export GOPATH=`pwd`
    go get challenge10
    go test challenge10
