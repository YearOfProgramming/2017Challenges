#include <iostream>
#include <string>
#include "include/BST.h"


/****************************************************************
 * CONSTRUCTOR
 *   Creates an empty binary tree
 ****************************************************************/
BST::BST() {
    root = NULL;
}

/****************************************************************
 * DESTRUCTOR
 *   Free all memory used by current tree
 ****************************************************************/
BST::~BST() {
    delete_children(root);
}


void BST::insert(int key) {
    // insert key to tree
    Node *new_node = new Node();
    new_node->data = key;
    new_node->left = NULL;
    new_node->right = NULL;

    Node *temp = root;
    Node *parent = NULL;

    while(temp != NULL) {
        parent = temp;
        if(key < temp->data) {
            temp = temp->left;
        } else {
            temp = temp->right;
        }

    }
    new_node->parent = parent;

    if(parent == NULL) {
        root = new_node;
    } else if ( key > parent->data) {
        parent->right = new_node;
    } else {
        parent->left = new_node;
    }
}

void BST::del(int key) {
    Node *node = BST::search(key);
    if(node != NULL) {
        if(node->left == NULL) {
            BST::transplant(node, node->right);
        } else if(node->right == NULL) {
            BST::transplant(node, node->left);
        } else{

            Node *min = BST::minimum(node->right);
            if(min->parent != node) {
                BST::transplant(node, min);
                min->right = node->right;
                min->right->parent = min;
            }
            BST::transplant(node, min);
            min->left = node->left;
            min->left->parent = min;
        }
        delete node;
    }
}

void BST::transplant(Node *u, Node *v) {
    // Replace subtree u with subtree v
    if(u->parent == NULL) {
        root = v;
    } else if (u == u->parent->left) {
        u->parent->left = v;
    } else{
        u->parent->right = v;
    }
    if(v != NULL) {
        v->parent = u->parent;
    }
}

Node *BST::successor(Node *node) {
    // Returns the nenodet number in order
    if(node->right != NULL) {
        return BST::minimum(node);
    }
    Node *successor = node->parent;
    while(successor != NULL && node == successor->right) {
        node = successor;
        successor = successor->parent;
    }
    return successor;
}

Node *BST::minimum(Node *node) {
    while(node->left != NULL) {
        node = node->left;
    }
    return node;
}

Node *BST::maximum(Node *node) {
    while(node->right != NULL) {
        node = node->right;
    }

    return node;
}

Node *BST::search(int key) {
    Node *current_node = root;
    while(current_node != NULL) {
        if(key > current_node->data) {
            current_node = current_node->right;
        } else if(key < current_node->data) {
            current_node = current_node->left;
        } else {
            return current_node;
        }
    }

    return current_node;
}


void BST::print(traversal_order order) {
    if(order == in_order_trav) {
        in_order(root);
    } else if(order == pre_order_trav) {
        pre_order(root);
    } else if(order==post_order_trav) {
        post_order(root);
    }
}

void BST::pre_order(Node *node) {
    if(node != NULL) {
        std::cout << node->data << std::endl;
        BST::pre_order(node->left);
        BST::pre_order(node->right);
    }
}

void BST::in_order(Node *node) {
    if(node != NULL) {
        BST::in_order(node->left);
        std::cout << node->data << std::endl;
        BST::in_order(node->right);
    }
}

void BST::post_order(Node *node) {
    if(node != NULL) {
        BST::post_order(node->left);
        BST::post_order(node->right);
        std::cout << node->data << std::endl;
    }
}

void BST::delete_children(Node *parent) {
    if(parent->left != NULL) {
        delete_children(parent->left);
    }

    if(parent->right != NULL) {
        delete_children(parent->right);
    }

    delete parent;
}
