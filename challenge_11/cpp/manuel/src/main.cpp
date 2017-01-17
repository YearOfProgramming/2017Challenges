#include <string>
#include <iostream>
#include "include/BST.h"

int main(int argc,char **argv) {

    // Create an empty Binary Search Tree
    BST Tree;

    std::string input;
    // First character of input is the command
    char command; 

    // Main loop
    while ( std::getline(std::cin, input) )
    {
        command = input[0];
        // if it's the end of input
        if(command == 'e') {
            return 0;
        }

        if (command == 'o' ) {
            // print out in order
            if (input[1] == 'i') {
                Tree.print(BST::in_order_trav);
                // print out pre order
            } else if (input[2] == 'r' ) {
                Tree.print( BST::pre_order_trav );
                // print out post order
            } else if (input[2] == 'o' ) { 
                Tree.print(BST::post_order_trav);
            }
        } else {
            int key = std::stoi(input.substr(1,input.size()-1));

            // insert key
            if (command == 'i') {
                Tree.insert(key);
            } else { // else delete from tree
                Tree.del(key);
            }

        }
    }

    return 0;
}
