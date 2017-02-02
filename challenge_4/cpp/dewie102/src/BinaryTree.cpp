#include "include/BinaryTree.h"

// Set root node to null to avoid errors
BST::BST () {
	m_root = nullptr;
}

// Call the delete tree function to free up memory
BST::~BST () {
	DeleteTree ();
}

void BST::CreateNode (int l_value) {
	if (m_root != nullptr) { // If the root node exsits call the create node function using the root as the starting point
		CreateNode (l_value, m_root);
	} else { // If the root node does not exsit, create it
		m_root = new Node;
		m_root->m_value = l_value;
		m_root->m_left = nullptr;
		m_root->m_right = nullptr;
	}
}

void BST::DeleteTree () {
	if (m_root != nullptr) { // If the root node is not null then start the recursive call to delete node starting at the root.
		DeleteTree (m_root);
	}
}

Node* BST::Search (int l_value) {
	return Search (l_value, m_root); // Search for a given value starting at the root.
}

void BST::PrintTree () {
	if (m_root != nullptr) {
		PrintTree (m_root); // Start a recursive call to print out the tree, starting at the root
	} else {
		std::cout << "Binary Tree is Empty" << std::endl;
	}
}

void BST::InvertTree () {
	if (m_root != nullptr) {
		InvertTree (m_root); // Start a recursive call to invert the tree, starting at the root
	}
}

void BST::CreateNode (int l_value, Node* l_leaf) {
	if (l_leaf != nullptr) { // Make sure hte leaf is not null to avoid access violations
		if (l_value > l_leaf->m_value) { // If the value is greater than, add it to the right of the tree
			if (l_leaf->m_right == nullptr) { // If the node to the right is null, create it there.
				Node* leaf = new Node;
				leaf->m_value = l_value;
				leaf->m_left = nullptr;
				leaf->m_right = nullptr;
				l_leaf->m_right = leaf;
			} else {
				CreateNode (l_value, l_leaf->m_right); // Else recursively check right.
			}
		} else if (l_value < l_leaf->m_value) { // If the value is less than, add it to the left of the tree
			if (l_leaf->m_left == nullptr) { // If the node to the left is null, create it there.
				Node* leaf = new Node;
				leaf->m_value = l_value;
				leaf->m_left = nullptr;
				leaf->m_right = nullptr;
				l_leaf->m_left = leaf;
			} else {
				CreateNode (l_value, l_leaf->m_left); // Else recursively check left.
			}
		} else {
			return;
		}
	}
}

void BST::DeleteTree (Node* l_leaf) {
	if (l_leaf != nullptr) {
		DeleteTree(l_leaf->m_left); // Recursively delete the left child node
		DeleteTree(l_leaf->m_right); // Recursively delete the right child node
		delete l_leaf; // Delete the current node
	}
}

Node* BST::Search (int l_value, Node* l_leaf) {
	if (m_root != nullptr) { // Make sure the root is not null
		if (l_leaf != nullptr) { // Make sure the node is not null
			if (l_leaf->m_value == l_value) { // if the node value is equal to the searched, return the node
				return l_leaf;
			} else {
				if (l_value > l_leaf->m_value) {
					Search (l_value, l_leaf->m_right); // If the value is greater than, check right child node
				} else if (l_value < l_leaf->m_value) {
					Search (l_value, l_leaf->m_left); // If the value is less than check left child node
				}
			}
		}
	}

	return nullptr;
}

void BST::PrintTree (Node* l_leaf) {
	if (l_leaf != nullptr) {
		if (l_leaf->m_left != nullptr) {
			PrintTree (l_leaf->m_left); // Recursively print left node
		}

		std::cout << l_leaf->m_value << " "; // Print current node value

		if (l_leaf->m_right != nullptr) {
			PrintTree (l_leaf->m_right); // Recursively print right node
		}
	}
}

void BST::InvertTree (Node* l_leaf) {
	if (l_leaf != nullptr) {

		InvertTree (l_leaf->m_left); // Recursively invert the left child nodes
		InvertTree (l_leaf->m_right); // Recursively inver the right child nodes

		Node* temp = l_leaf->m_left; // Temp node for storage of the left node.
		l_leaf->m_left = l_leaf->m_right; // Switch the left node for the right node
		l_leaf->m_right = temp; // Set the right node equal to the temp
	}

	return;
}
