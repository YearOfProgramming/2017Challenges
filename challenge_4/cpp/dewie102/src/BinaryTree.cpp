#include "include/BinaryTree.h"

BST::BST () {
	m_root = nullptr;
}

BST::~BST () {
	DeleteTree ();
}

void BST::CreateNode (int l_value) {
	if (m_root != nullptr) {
		CreateNode (l_value, m_root);
	} else {
		m_root = new Node;
		m_root->m_value = l_value;
		m_root->m_left = nullptr;
		m_root->m_right = nullptr;
	}
}

void BST::DeleteTree () {
	if (m_root != nullptr) {
		DeleteTree (m_root);
	}
}

Node* BST::Search (int l_value) {
	return Search (l_value, m_root);
}

void BST::PrintTree () {
	if (m_root != nullptr) {
		PrintTree (m_root);
	} else {
		std::cout << "Binary Tree is Empty" << std::endl;
	}
}

void BST::InvertTree () {
	if (m_root != nullptr) {
		InvertTree (m_root);
	}
}

void BST::CreateNode (int l_value, Node* l_leaf) {
	if (l_leaf != nullptr) {
		if (l_value > l_leaf->m_value) {
			if (l_leaf->m_right == nullptr) {
				Node* leaf = new Node;
				leaf->m_value = l_value;
				leaf->m_left = nullptr;
				leaf->m_right = nullptr;
				l_leaf->m_right = leaf;
			} else {
				CreateNode (l_value, l_leaf->m_right);
			}
		} else if (l_value < l_leaf->m_value) {
			if (l_leaf->m_left == nullptr) {
				Node* leaf = new Node;
				leaf->m_value = l_value;
				leaf->m_left = nullptr;
				leaf->m_right = nullptr;
				l_leaf->m_left = leaf;
			} else {
				CreateNode (l_value, l_leaf->m_left);
			}
		} else {
			return;
		}
	}
}

void BST::DeleteTree (Node* l_leaf) {
	if (l_leaf != nullptr) {
		if (l_leaf->m_left != nullptr) {
			DeleteTree (l_leaf->m_left);
		}

		if (l_leaf->m_right != nullptr) {
			DeleteTree (l_leaf->m_right);
		}
	}
}

Node* BST::Search (int l_value, Node* l_leaf) {
	if (m_root != nullptr) {
		if (l_leaf != nullptr) {
			if (l_leaf->m_value == l_value) {
				return l_leaf;
			} else {
				if (l_value > l_leaf->m_value) {
					Search (l_value, l_leaf->m_right);
				} else if (l_value < l_leaf->m_value) {
					Search (l_value, l_leaf->m_left);
				}
			}
		}
	}

	return nullptr;
}

void BST::PrintTree (Node* l_leaf) {
	if (l_leaf != nullptr) {
		if (l_leaf->m_left != nullptr) {
			PrintTree (l_leaf->m_left);
		}

		std::cout << l_leaf->m_value << " ";

		if (l_leaf->m_right != nullptr) {
			PrintTree (l_leaf->m_right);
		}
	}
}

void BST::InvertTree (Node* l_leaf) {
	if (l_leaf != nullptr) {

		InvertTree (l_leaf->m_left);
		InvertTree (l_leaf->m_right);

		Node* temp = l_leaf->m_left;
		l_leaf->m_left = l_leaf->m_right;
		l_leaf->m_right = temp;
	}

	return;
}