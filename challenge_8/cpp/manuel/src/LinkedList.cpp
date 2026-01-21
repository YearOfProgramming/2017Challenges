#include <string>
#include <map>

#include "include/LinkedList.h"

LinkedList::Node * LinkedList::copy(Node *root) {
    // Assumes passed in node is prebuilt
    // linked list and copies the data on it
    // onto a new linked list
    
    std::map<Node *, Node *> copies; // Maps old nodes to their copy

    Node *temp = root; // Pointer to root node

    // Allocate new memory for copy
    while(temp != NULL) {
        copies[temp] = new Node();
        temp = temp->next;
    }

    // Reset list
    temp = root;
    Node *copy;

    // Copy data
    while(temp->next != NULL) {
        copy = copies[temp];
        copy->next = copies[temp->next];
        copy->random = copies[temp->random];
        copy->data = temp->data + "'";
        temp = temp->next;
    }
    return copies[root];
}

void LinkedList::clean(Node *root) {
    // Frees the used memory by nodes
    Node *temp = root->next;
    
    while(temp != NULL) {
        root->next = temp->next;
        temp->next = NULL;
        temp->random = NULL;
        delete temp;
        temp = root->next;
    }
}
