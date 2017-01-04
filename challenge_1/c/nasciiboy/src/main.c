#include <stdio.h>

void reverseString( char *str ){
  if( *str ){
    reverseString( str + 1 );
    putchar( *str );
  }
}

int main( int argc, char *argv[] ){
  if( argc == 1 ) return 1;

  reverseString( argv[ 1 ] );
  putchar( '\n' );

  return 0;
}
