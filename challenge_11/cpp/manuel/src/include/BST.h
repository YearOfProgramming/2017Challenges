#ifndef BST_H
#define BST_H

// Representation of an element in the tree
struct Node {
  int data;   // Value of the node
  Node *left;   // Pointer to the left node
  Node *right;  // Pointer to the right node
  Node *parent; // Pointer to the parent node
};

class BST {
  // Public Definitions
  public: 
	  enum traversal_order { in_order_trav, pre_order_trav, post_order_trav };

  // Public Functions/Variables
  public:
    BST();  // Constructor
   ~BST(); // Destructor
    void insert(int key);
    void del(int key);
    void print(enum traversal_order);

  // Private Functions/Variables
  private:
    Node *root;

    Node *search(int key); // Searche for a node in the tree
    Node *successor(Node *current_node); // Find the successor of the given node
    Node *minimum(Node *current_node); // Find the minimum node of the given subtree
    Node *maximum(Node *current_node); // Find the minimum node of the given subtree
    void transplant(Node *u, Node *v); // Replace the subtree rooted at node u with the subtree rooted at node v
    void in_order(Node *current_node); // Inorder traversal
    void pre_order(Node *current_node); // Preorder traversal
    void post_order(Node *current_node); // Postorder traversal
    void delete_children(Node *parent); // Deletes all children recursively
};

#endif
