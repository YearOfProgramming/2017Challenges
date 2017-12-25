#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  struct node *leftNode;
  int data;
  unsigned int count;
  struct node *rightNode;
} TreeNode;

const int TREENODE_SIZE = sizeof( TreeNode );

void appendNodes( TreeNode **ptrNode, int data[], int size );
void appendNode( TreeNode **ptrTreeNode, int data );
void showMajorityElement( TreeNode *ptrTreeNode, int majority );
void freeNode( TreeNode **ptrTreeNode );
void showArray( int data[], int size );

int main(){
  TreeNode *rootNode = NULL;
  int data[37] = {2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7};

  showArray( data, 37 );

  appendNodes( &rootNode, data, 37 );
  showMajorityElement( rootNode, 37/2 );
  freeNode( &rootNode );

  return 0;
}

void showArray( int data[], int size ){
  printf( "Data = [ " );
  for( int i = 0; i < size; i++ )
    printf( "%d ", data[i] );

  printf( "]\n" );
}

void appendNodes( TreeNode **ptrNode, int data[], int size ){
  for( int i = 0; i < size; i++ )
    appendNode( ptrNode, data[i] );
}

void appendNode( TreeNode **ptrTreeNode, int data ){
  if ( *ptrTreeNode == NULL ){
    *ptrTreeNode = malloc( TREENODE_SIZE );

    if ( *ptrTreeNode != NULL ){
      (*ptrTreeNode)->count     = 1;
      (*ptrTreeNode)->data      = data;
      (*ptrTreeNode)->leftNode  = NULL;
      (*ptrTreeNode)->rightNode = NULL;
    } else
      fprintf( stderr, "No memory available. Can not be added %d.\n", data );
  } else {
    if ( data < (*ptrTreeNode)->data )
      appendNode( &((*ptrTreeNode)->leftNode), data );
    else if ( data > (*ptrTreeNode)->data )
      appendNode( &((*ptrTreeNode)->rightNode), data );
    else
      (*ptrTreeNode)->count++;
  }
}

void showMajorityElement( TreeNode *ptrTreeNode, int majority ){
  if ( ptrTreeNode == NULL ) return;

  if( ptrTreeNode->count >= majority )
    printf( "Majority Element: %d\n"
            "           Times: %d\n",
            ptrTreeNode->data, ptrTreeNode->count );

  showMajorityElement( ptrTreeNode->leftNode, majority );
  showMajorityElement( ptrTreeNode->rightNode, majority );
}

void freeNode( TreeNode **ptrTreeNode ){
  if ( (*ptrTreeNode) == NULL ) return;

  freeNode( &((*ptrTreeNode)->leftNode) );
  freeNode( &((*ptrTreeNode)->rightNode) );
  free( *ptrTreeNode );
  *ptrTreeNode = NULL;
}
