package main

import (
    "fmt"
    "os"
    "bufio"
)

func strrev(s string) string {
    r := []rune(s)
    rs := []rune{}
    for i := len(r)-1; i>=0; i-- {
        rs = append(rs, r[i])
    }
    return string(rs)
}

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        fmt.Println(strrev(scanner.Text()))
    }
}