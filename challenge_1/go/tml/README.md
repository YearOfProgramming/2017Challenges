# golang: Reverse a string

## My thought process
I don't want to do it in bytes - I want to use the runes support in golang
OK, so this range thing looks useful (blog link)
On second thought, maybe not - it's going to give me a value I have no use for
OK, let's try this normalization package (blog link)
But slow - oh, well
OK, so now my string has to become a range of bytes
http://devs.cloudimmunity.com/gotchas-and-common-mistakes-in-go-golang/ looks good