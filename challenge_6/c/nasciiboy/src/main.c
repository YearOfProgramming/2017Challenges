#include <stdio.h>
#include <stdlib.h>

int main( int argc, char *argv[] ){
  printf( "Input: [" );
  for( int i = 1; i < argc; i++ )
    printf( "%s%s", argv[ i ], i + 1 == argc ? "" : "," );
  puts( "]" );

  puts( "Ranges:" );
  for( int i = 1; i < argc; ){
    int init  = atoi( argv[ i ] );
    int last  = init;
    int next  = init + 1;

    for( i++; i < argc && next == atoi( argv[ i ] ); i++ )
      last = next++;

    if( last > init ) printf( "%d ==> %d\n", init, last );
  }
  putchar( '\n' );

  return 0;
}
