#include <stdio.h>

char * strCmp( char *s1, char *s2 ){
  for( ; *s1; s1++, s2++ )
    if( *s1 != *s2 ) return s2;

  if( *s2 ) return s2;

  return 0;
}

int main( int argc, char *argv[] ){
  if( argc < 3 ) return 1;

  char *diff = strCmp( argv[1], argv[2] );

  printf( "Input:\ns = %s\nt = %s\n\n", argv[1], argv[2] );

  if( diff ) printf( "Output:\n[%c]\n", *diff );
  else       printf( "s == t\n" );

  return 0;
}
