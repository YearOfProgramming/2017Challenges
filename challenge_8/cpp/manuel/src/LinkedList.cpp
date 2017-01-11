#include <string>
#include <vector>
#include <stdlib.h> /*srand, rand */
#include <time.h> 
#include <algorithm> // std::remove
#include <map>
#include <cstddef> // ptrdiff_t

#include "include/LinkedList.h"

LinkedList::LinkedList() {
    head = NULL;
    current_node = head;
    prev_node = NULL;
    members =  new std::vector<Node *>;

    // Array is linked list in reverse
    members->push_back(head);
}

LinkedList::LinkedList(std::vector<Node *> *new_members) {
    head = (*new_members)[members->size() - 1];
    current_node = head;
    prev_node = NULL;
    members = new_members;
}

LinkedList::~LinkedList() {
    for(Node *i:*members){
        delete i;
    }

    delete[] members;
}

std::string LinkedList::data() {
    return current_node->data;
}

void LinkedList::insert(std::string data) {
    // Inserts node to front of list
    // Resets random pointers to new nodes

    Node *new_node = new Node();
    new_node->data = data;
    new_node->next = head;
    members->push_back(new_node);
    head = new_node;

    // Randomise all nodes again
    while(new_node != NULL) {
        set_random(new_node);
        new_node = new_node->next;
    }


}

std::string LinkedList::pop() {
    // Pops off current node from list

    // Remove from members list
    members->erase(std::remove(members->begin(), members->end(), current_node), members->end());

    // Connect previous and next node
    std::string data = current_node->data;
    prev_node->next = current_node->next;

    delete current_node;
    return data; 
}

bool LinkedList::next() {
    if(current_node->next != NULL) {
        prev_node = current_node;
        current_node = current_node->next;
        return true;
    } 

    return false;
}

void LinkedList::random() {
    // Jump to random node!

    srand(time(NULL));
    int index = members->size() - 1;
    index = rand() % index;

    if(index == 0) {
        prev_node = NULL;
    } else {
        prev_node = (*members)[index - 1];
    }

    current_node = (*members)[index];
}
    

void LinkedList::set_random(Node *node) {

    srand(time(NULL));
    int index = members->size() - 1;
    index = rand() % index;
    node->random = (*members)[index];
}

LinkedList * LinkedList::deep_copy() {
    int length = members->size();
    std::vector<Node *> *new_members = new std::vector<Node *>();

    for(int i = 0; i < length; i++) {
        Node *node = new Node();
        node->data = std::string((*members)[i]->data + "'");
        new_members->push_back(node);
    }

    ptrdiff_t random_index;
    Node *random_node;
    for(int j = 0; j < length; j++) {
       random_node = (*members)[j]->next;

       random_index = std::distance (members->begin(),
               std::find(members->begin(), members->end(), random_node));
       
       (*new_members)[j]->random = (*new_members)[random_index];

       if(j - 1 >= 0) {
           (*new_members)[j]->next = (*new_members)[j - 1];
       } else {
           (*new_members)[j]->next = NULL;
       }
    }

    return new LinkedList(new_members);
}
