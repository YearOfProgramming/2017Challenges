#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  struct node *leftNode;
  int data;
  struct node *rightNode;
} TreeNode;

const int TREENODE_SIZE = sizeof( TreeNode );

void appendNode ( TreeNode **ptrTreeNode, int data );
void showNode   ( TreeNode  *ptrTreeNode, int deep );
void freeNode   ( TreeNode **ptrTreeNode );
void invertNode ( TreeNode  *ptrTreeNode );

int main( int argc, char *argv[] ){
  TreeNode *rootNode = NULL;

  for( int i = 1; i < argc; i++ )
    appendNode( &rootNode, atoi( argv[ i ] ) );

  printf( "In Order:\n\n" );
  showNode( rootNode, 0 );

  printf( "\nInverse Order:\n\n" );
  invertNode( rootNode );
  showNode( rootNode, 0 );
  putchar( '\n' );

  freeNode( &rootNode );

  return 0;
}

void appendNode( TreeNode **ptrTreeNode, int data ){
  if ( *ptrTreeNode == NULL ){
    *ptrTreeNode = malloc( TREENODE_SIZE );

    if ( *ptrTreeNode != NULL ){
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
    else {
      // repeat data
    }
  }
}

void showNode( TreeNode *ptrTreeNode, int deep ){
  if ( ptrTreeNode == NULL ) return;

  showNode( ptrTreeNode->leftNode , deep + 1 );

  for( int i = 0; i < deep; i++ )
    printf( "    " );
  printf( "|-%3d\n", ptrTreeNode->data );

  showNode( ptrTreeNode->rightNode, deep + 1 );
}

void invertNode( TreeNode *ptrTreeNode ){
  if ( ptrTreeNode == NULL ) return;

  invertNode( ptrTreeNode->leftNode  );
  invertNode( ptrTreeNode->rightNode );

  TreeNode *tmp =  ptrTreeNode->leftNode;
  ptrTreeNode->leftNode  = ptrTreeNode->rightNode;
  ptrTreeNode->rightNode = tmp;
}

void freeNode( TreeNode **ptrTreeNode ){
  if ( (*ptrTreeNode) == NULL ) return;

  freeNode( &((*ptrTreeNode)->leftNode ) );
  freeNode( &((*ptrTreeNode)->rightNode) );
  free( *ptrTreeNode );
  *ptrTreeNode = NULL;
}
