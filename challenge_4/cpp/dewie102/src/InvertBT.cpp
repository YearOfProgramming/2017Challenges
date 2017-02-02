#include "include/BinaryTree.h"
#include <iostream>

int main (int argc, char** argv) {
	// Create the tree how you want it to look. 4 is going to be the root and then it will separate greater than goes "right"
	// and less than goes "left"
	BST tree;
	tree.CreateNode (4);
	tree.CreateNode (2);
	tree.CreateNode (7);
	tree.CreateNode (1);
	tree.CreateNode (3);
	tree.CreateNode (9);
	tree.CreateNode (6);
	
	// Print out the original tree before inversion
	std::cout << "Original Tree: ";
	tree.PrintTree ();
	std::cout << std::endl;

	tree.InvertTree (); // Successfully invert the tree
	
	// Print out the inverted tree.
	std::cout << "Inverse Tree: ";
	tree.PrintTree ();
	std::cout << std::endl;

	return 0;
}
