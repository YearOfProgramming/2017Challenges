#ifndef LINKEDLIST_H
#define LINKEDLIST_H

class LinkedList {

    public:

        struct Node {
            std::string data;
            Node *next;
            Node *random;
        };

        static Node * copy(Node *);
        static void clean(Node *);
};

#endif
