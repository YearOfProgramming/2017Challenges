#include "../src/binary_tree.h"

/* Start add Tests */
void add_null_tree()
{
  printf("Test calling add with null BinaryTree.\n");
  add(NULL, 4);
  printf("No error. Test Pass.\n");
}

void add_no_root()
{
  printf("Test calling add on a tree which does not have a root node.\n");
  struct BinaryTree testTree;
  add(&testTree, 1);

  if (testTree.root == NULL)
  {
    printf("Root tree is still null. Test Fail.\n");
  }
  else if (testTree.root->data == 1)
  {
    printf("1 was added to tree in root node. Test Pass\n");
  }
  else
  {
    printf("Expected root data to be 1, but was %d\n", testTree.root->data);
  }

  free_tree(testTree);
}

void add_less_than_root()
{
  printf("Test adding value to tree which is less than root value.\n");
  struct BinaryTree testTree;
  add(&testTree, 3);
  add(&testTree, 1);

  if (testTree.root->left == NULL)
  {
    printf("Root's left is null. Test Fail.\n");
  }
  else if (testTree.root->left->data == 1)
  {
    printf("1 was added to tree in Root's left node. Test Pass\n");
  }
  else
  {
    printf("Expected Root's left data to be 1, but was %d\n",
      testTree.root->left->data);
  }

  free_tree(testTree);
}

void add_greater_than_root()
{
  printf("Test adding value to tree which is greater than root value.\n");
  struct BinaryTree testTree;
  add(&testTree, 0);
  add(&testTree, 1);

  if (testTree.root->right == NULL)
  {
    printf("Root's right is null. Test Fail.\n");
  }
  else if (testTree.root->right->data == 1)
  {
    printf("1 was added to tree in Root's right node. Test Pass\n");
  }
  else
  {
    printf("Expected Root's right data to be 1, but was %d\n",
      testTree.root->right->data);
  }

  free_tree(testTree);
}

void add_equal_to_root()
{
  printf("Test calling add oon an element which is already in tree\n");
  struct BinaryTree testTree;
  add(&testTree, 0);
  add(&testTree, 0);

  if (testTree.root->right == NULL && testTree.root->left == NULL)
  {
    printf("No data added. Test Pass\n");
  }
  else if (testTree.root->right != NULL)
  {
    printf("Data was added to right of root. Test Fail\n");
  }
  else
  {
    printf("Data was added to left of root. Test Fail\n");
  }

  free_tree(testTree);
}

/* End add Tests */

/* Start print_tree Tests */
void print_tree_empty_tree()
{
  printf("Test printing empty tree. Expect nothing to be printed below.\n");
  struct BinaryTree testTree;
  print_tree(testTree);
}

void print_tree_filled()
{
  printf("Test printing tree from Readme.MD. Expect output to be 6 3 9 2 4 7 10\n");
  struct BinaryTree testTree;
  add(&testTree, 6);
  add(&testTree, 3);
  add(&testTree, 9);
  add(&testTree, 2);
  add(&testTree, 4);
  add(&testTree, 7);
  add(&testTree, 10);
  print_tree(testTree);

  free_tree(testTree);
}
/* End print_tree Tests */

/* Start reverse Tests */
void reverse_null_tree()
{
  printf("Test calling reverse with null BinaryTree.\n");
  reverse(NULL);
  printf("No error. Test Pass.\n");
}

void reverse_empty_tree()
{
  printf("Test calling reverse on a tree which does not have a root node.\n");
  struct BinaryTree testTree;
  reverse(&testTree);

  if (testTree.root == NULL)
  {
    printf("Root node is still null. Test Pass.\n");
  }
  else
  {
    printf("Root node is not null. Test Fail.\n");
  }
}

void reverse_tree_works()
{
  printf("Test reversing tree which is imbalanced.\n");
  /* Create tree
        6
       / \
      3   9
     / \  \
    2  4  10
  */
  struct BinaryTree testTree;
  add(&testTree, 6);
  add(&testTree, 3);
  add(&testTree, 2);
  add(&testTree, 4);
  add(&testTree, 9);
  add(&testTree, 10);

  /* Expect tree
        6
       / \
      9   3
     /   / \
    10  4  2
  */

  printf("Expect output below to be 6 9 3 10 4 2\n");
  print_tree(testTree);

  free_tree(testTree);
}

/* End reverse Tests */

// Main method
int main(int argc, char** argv)
{
  printf("Start add tests\n");
  add_null_tree();
  add_no_root();
  add_greater_than_root();
  add_less_than_root();
  add_equal_to_root();
  printf("End add tests\n");

  printf("Start print_tree tests\n");
  print_tree_empty_tree();
  print_tree_filled();
  printf("End print_tree tests\n");

  printf("Start reverse tests\n");
  reverse_null_tree();
  reverse_empty_tree();
  reverse_tree_works();
  printf("End reverse tests\n");
}
