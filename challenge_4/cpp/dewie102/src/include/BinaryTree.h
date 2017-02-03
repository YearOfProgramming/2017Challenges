#pragma once
#include <iostream>

struct Node {
	Node* m_right;
	Node* m_left;
	int m_value;
};

class BST {
public:
	BST ();
	~BST ();

	void CreateNode (int l_value);
	void DeleteTree ();

	Node* Search (int l_value);
	void PrintTree ();
	void InvertTree ();
private:
	void CreateNode (int l_value, Node* l_leaf);
	void DeleteTree (Node* l_leaf);

	Node* Search (int l_value, Node* l_leaf);
	void PrintTree (Node* l_leaf);
	void InvertTree (Node* l_leaf);

	Node* m_root;
};