# unintq

Show items that are not repeated in an array

## How this program works

With a binary tree and arrays that specify what type of data are

``` c
typedef struct {
  int32_t data;
  Type type;
} MixData;
```

`Type = TINT` to ints, and `Type = TCHAR` to chars.

## Building

``` bash
make
```

## Running

``` bash
make test
```

## Cleanup

``` bash
make clean
```
