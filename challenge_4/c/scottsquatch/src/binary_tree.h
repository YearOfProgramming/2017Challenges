// Minimal BinaryTree. Only implement methods necessary for solving
// problem 3.
#ifndef _BINARY_TREE_H_
#define _BINARY_TREE_H_

#include <stdio.h>
#include <stdlib.h>

/* Structs */
struct Node
{
  int data;
  struct Node* left;
  struct Node* right;
};

struct BinaryTree
{
  struct Node* root;
};

/* Method Prototypes */
void add(struct BinaryTree*, int);
struct Node* add_recurse(struct Node*, int);
void print_tree(struct BinaryTree);
void print_tree_recurse(struct Node*);
void reverse(struct BinaryTree*);
struct Node* reverse_recurse(struct Node*);
void free_tree(struct BinaryTree);
void free_node_recurse(struct Node*);

// Add the given data to the tree.
void add(struct BinaryTree* tree, int data)
{
  // if tree is null, then there is nothing to do
  if (tree != NULL)
  {
    tree->root = add_recurse(tree->root, data);
  }
}

// Recursive method call
struct Node* add_recurse(struct Node* parentNode, int data)
{
  // base case
  if (parentNode == NULL)
  {
    // Sweet we can create the new node now
    parentNode = calloc(1, sizeof(struct Node));
    parentNode->data = data;

    return parentNode;
  }

  // Determine whether to add to left or right pointer.
  if (data < parentNode->data)
  {
    parentNode->left = add_recurse(parentNode->left, data);
  }
  else if (data > parentNode->data)
  {
    parentNode->right = add_recurse(parentNode->right, data);
  }

  // Return this node as this is a r
  return parentNode;
}

// Print the tree using Breadth-First traversal
void print_tree(struct BinaryTree tree)
{
  // Breadth-First traversal
  print_tree_recurse(tree.root);
}

void print_tree_recurse(struct Node* node)
{
  // base case
  if (node == NULL)
  {
    return;
  }

  printf("%d ", node->data);
  print_tree_recurse(node->left);
  print_tree_recurse(node->right);
}

// Reverse BinaryTree.
void reverse(struct BinaryTree* tree)
{
  tree->root = reverse_recurse(tree->root);
}

// Reverse left and right trees
struct Node* reverse_recurse(struct Node* node)
{
  // base case
  if (node != NULL)
  {
    // switch left and right trees
    struct Node* temp = node->left;
    node->left = reverse_recurse(node->right);
    node->right = reverse_recurse(temp);
  }

  return node;
}

// Free memory used by BinaryTree
void free_tree(struct BinaryTree tree)
{
  // Recursive deletion
  free_node_recurse(tree.root);
}

void free_node_recurse(struct Node* node)
{
  // base case
  if (node != NULL)
  {
    // Need to free children before freeing yourself
    free_node_recurse(node->left);
    free_node_recurse(node->right);

    free(node);
  }
}

#endif
