# Challenge 12: Compression and Decompression

## 1. Solution Description

This challenge is all about run length encoding (RLE).

Encode() counts consecutive runs of a single character. If multiple are encountered it adds the character, a pound sign, and the number of occurrences to the output buffer. Single characters are directly transfered to the output buffer.

Decode() has to reverse this but in doing so has to handle more error conditions due to malformed input. Otherwise it detects if a pound sign immediately follows the current character and if so expands that character out the appropriate count into the output buffer.

## 2. Running Tests

In bash in this directory:

    export GOPATH=`pwd`
    go test c12
