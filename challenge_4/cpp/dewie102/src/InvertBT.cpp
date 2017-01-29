#include "include/BinaryTree.h"
#include <iostream>

int main (int argc, char** argv) {
	BST tree;
	tree.CreateNode (4);
	tree.CreateNode (2);
	tree.CreateNode (7);
	tree.CreateNode (1);
	tree.CreateNode (3);
	tree.CreateNode (9);
	tree.CreateNode (6);
	
	std::cout << "Original Tree: ";
	tree.PrintTree ();
	std::cout << std::endl;

	tree.InvertTree ();

	std::cout << "Inverse Tree: ";
	tree.PrintTree ();
	std::cout << std::endl;

	return 0;
}