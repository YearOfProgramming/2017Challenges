#include <iostream>

#include "include/LinkedList.h"

int main(int argc, char **argv) {
    LinkedList::Node *list = new LinkedList::Node();
    
    // Build dummy list
    LinkedList::Node *temp = list;
    for(char letter = 'A'; letter <= 'Z';  letter++) {
       temp->data = letter;
       temp->next = new LinkedList::Node();
       temp = temp->next;
    }

    // Iterate through list
    temp = list;
    while(temp != NULL) {
        std::cout << temp->data << " ";
        temp = temp->next;
    }
    std::cout << std::endl;

    // Make copy
    LinkedList::Node *copy = LinkedList::copy(list);

    // Iterate through copy
    temp = copy;
    while(temp != NULL) {
        std::cout << temp->data << " ";
        temp = temp->next;
    }
    std::cout << std::endl;

    LinkedList::clean(list); // deallocate memory
    LinkedList::clean(copy);
    delete copy;
    delete list;
    return 0;
}
       
