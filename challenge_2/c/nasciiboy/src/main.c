#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

typedef enum { INT, CHAR, MIX, INTD, CHARD, MIXD, MIXID, MIXCD } Flags;
typedef enum { TINT, TCHAR } Type;

typedef struct {
  int32_t data;
  Type type;
} MixData;

typedef struct node {
  struct node *leftNode;
  int32_t data;
  Flags flags;
  struct node *rightNode;
} TreeNode;

const uint8_t TREENODE_SIZE = sizeof( TreeNode );

void appendNodes( TreeNode **ptrTreeNode, MixData data[], uint32_t size );
void appendNode( TreeNode **ptrTreeNode, int data, Type type );
void freeNode( TreeNode **ptrTreeNode );

// UnicodeToUTF8() from http://stackoverflow.com/questions/19968705/unsigned-integer-as-utf-8-value
void UnicodeToUTF8( uint32_t codepoint, char str[] );
void nodeShowData( TreeNode *ptrTreeNode );
void showUniqNodes( TreeNode *ptrTreeNode );
void showMixData( MixData data[], uint32_t size );

int main(){
  TreeNode *ptrRaiz = NULL;
  MixData intData[18] = { {2,TINT},{3,TINT},{4,TINT},{2,TINT},{3,TINT},{5,TINT},{4,TINT},{6,TINT},{4,TINT},{6,TINT},{9,TINT},{10,TINT},{9,TINT},{8,TINT},{7,TINT},{8,TINT},{10,TINT},{7,TINT}};
  MixData mixData[26] = {{2,TINT},{u'a',TCHAR},{u'l',TCHAR},{3,TINT},{u'l',TCHAR},{4,TINT},{u'k',TCHAR},{2,TINT},{3,TINT},{4,TINT},{u'a',TCHAR},{6,TINT},{u'c',TCHAR},{4,TINT},{u'm',TCHAR},{6,TINT},{u'm',TCHAR},{u'k',TCHAR},{9,TINT},{10,TINT},{9,TINT},{8,TINT},{7,TINT},{8,TINT},{10,TINT},{7,TINT}};

  showMixData( intData, 18 );
  printf( "unics: " );
  appendNodes( &ptrRaiz, intData, 18 );
  showUniqNodes( ptrRaiz );
  freeNode( &ptrRaiz );
  putchar( '\n' );

  showMixData( mixData, 26 );
  printf( "unics: " );
  appendNodes( &ptrRaiz, mixData, 26 );
  showUniqNodes( ptrRaiz );
  freeNode( &ptrRaiz );
  putchar( '\n' );

  return 0;
}

void showMixData( MixData data[], uint32_t size ){
  printf( "Data = [ " );
  for( int i = 0; i < size; i++ )
    if( data[i].type == TINT )
      printf( "%d ", data[i].data );
    else {
      char str[5] = { 0 };
      UnicodeToUTF8( data[i].data, str );
      printf( "%.4s ", str );
   }

  printf( "]\n" );
}

void appendNodes( TreeNode **ptrNode, MixData data[], uint32_t size ){
  for( int i = 0; i < size; i++ )
    appendNode( ptrNode, data[i].data, data[i].type );
}

void appendNode( TreeNode **ptrTreeNode, int data, Type type ){
  if ( *ptrTreeNode == NULL ){
    *ptrTreeNode = malloc( TREENODE_SIZE );

    if ( *ptrTreeNode != NULL ){
      (*ptrTreeNode)->data      = data;
      (*ptrTreeNode)->flags     = type;
      (*ptrTreeNode)->leftNode  = NULL;
      (*ptrTreeNode)->rightNode = NULL;
    } else
      fprintf( stderr, "No memory available. Can not be added %d.\n", data );
  } else {
    if ( data < (*ptrTreeNode)->data )
      appendNode( &((*ptrTreeNode)->leftNode), data, type );
    else if ( data > (*ptrTreeNode)->data )
      appendNode( &((*ptrTreeNode)->rightNode), data, type );
    else
      switch( (*ptrTreeNode)->flags ){
      case INT  :
        (*ptrTreeNode)->flags = type == TINT  ?  INTD : MIX;
        break;
      case CHAR :
        (*ptrTreeNode)->flags = type == TCHAR ? CHARD : MIX;
        break;
      case MIX  :
        (*ptrTreeNode)->flags = type == TINT  ? MIXID : MIXCD;
        break;
      case INTD :
        (*ptrTreeNode)->flags = type == TCHAR ? MIXID : INTD;
        break;
      case CHARD:
        (*ptrTreeNode)->flags = type == TINT  ? MIXCD : CHARD;
        break;
      case MIXID:
        (*ptrTreeNode)->flags = type == TCHAR ? MIXD  : MIXID;
        break;
      case MIXCD:
        (*ptrTreeNode)->flags = type == TINT  ? MIXD  : MIXCD;
        break;
      case MIXD : break;
      }
  }
}

void freeNode( TreeNode **ptrTreeNode ){
  if ( (*ptrTreeNode) == NULL ) return;

  freeNode( &((*ptrTreeNode)->leftNode) );
  freeNode( &((*ptrTreeNode)->rightNode) );
  free( *ptrTreeNode );
  *ptrTreeNode = NULL;
}

void showUniqNodes( TreeNode *ptrTreeNode ){
  if ( ptrTreeNode == NULL ) return;

  nodeShowData( ptrTreeNode );
  showUniqNodes( ptrTreeNode->leftNode );
  showUniqNodes( ptrTreeNode->rightNode );
}

void nodeShowData( TreeNode *ptrTreeNode ){
  char str[5] = { 0 };

  switch( ptrTreeNode->flags ){
  case INT  :
    printf( "%d ", ptrTreeNode->data );
    break;
  case CHAR :
    UnicodeToUTF8( ptrTreeNode->data, str );
    printf( "\'%.4s\' ", str );
    break;
  case MIX  :
    printf( "%d ", ptrTreeNode->data );
    UnicodeToUTF8( ptrTreeNode->data, str );
    printf( "\'%.4s\' ", str );
    break;
  case INTD :
  case CHARD:
    break;
  case MIXID:
    UnicodeToUTF8( ptrTreeNode->data, str );
    printf( "\'%.4s\' ", str );
    break;
  case MIXCD:
    printf( "%d ", ptrTreeNode->data );
    break;
  case MIXD : break;
  }
}

void UnicodeToUTF8( uint32_t codepoint, char str[] ){
  if( codepoint <= 0x7f )
    str[0] = codepoint;
  else if( codepoint <= 0x7ff ){
    str[0] = 0xc0 | ((codepoint >> 6) & 0x1f);
    str[1] = 0x80 | (codepoint & 0x3f);
  } else if( codepoint <= 0xffff ){
    str[0] = 0xe0 | ((codepoint >> 12) & 0x0f);
    str[1] = 0x80 | ((codepoint >> 6) & 0x3f);
    str[2] = 0x80 | (codepoint & 0x3f);
  } else {
    str[0] = 0xf0 | ((codepoint >> 18) & 0x07);
    str[1] = 0x80 | ((codepoint >> 12) & 0x3f);
    str[2] = 0x80 | ((codepoint >> 6) & 0x3f);
    str[4] = 0x80 | (codepoint & 0x3f);
  }
}
