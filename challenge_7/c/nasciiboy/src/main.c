#include <stdio.h>
#include <stdlib.h>

int sumOfRange( int a, int b ){
  int n = b - a + 1;
  int nSum = n * (n + 1) / 2;
  int bSum = (a - 1) * n;

  return nSum + bSum;
}

int main( int argc, char *argv[] ){
  if( argc < 2 ) {
    fprintf( stderr, "Usage: FindMissing val1 val2 ...\n" );
    return 0;
  }

  int sum = atoi( argv[1] );
  printf( "Input: [%d,", sum );

  int min = sum, max = sum;
  for( int i = 2, n; i < argc; i++ ){
    printf( "%s%s", argv[ i ], i + 1 == argc ? "" : "," );

    n = atoi( argv[i] );
    sum += n;

    if( n > max ) max = n;
    if( n < min ) min = n;
  }

  puts( "]" );

  int sRange = sumOfRange( min, max );
  printf( "The missing number is: %d\n", sRange - sum  );

  return 0;
}
