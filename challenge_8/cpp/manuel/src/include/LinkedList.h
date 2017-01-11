#ifndef LINKED_LIST_H
#define LINKED_LIST_H

class LinkedList {

    public:

        struct Node {
            std::string data;
            Node *next;
            Node *random;
        };

        LinkedList();
        LinkedList(std::vector<Node *> *);
        ~LinkedList();

        std::string data();
        void insert(std::string);
        std::string pop();
        bool next();
        void random();
        void set_random(Node *);
        LinkedList * deep_copy();

    private:

        Node *head;
        Node *prev_node;
        Node *current_node;

        // Stores pointers to all nodes in linked list
        std::vector<Node *> *members; 
};

#endif
