#ifndef TREEINVERSION_h
#define TREEINVERSION_h

std::vector<int> stringToDigits (std::string stringDigits);
struct node * buildTree(std::vector<int>);
void build(std::vector<int>, int, struct node *);
void invertTree(struct node *);
void print(struct node *node);

struct node {
    int value;
    struct node *leftChild;
    struct node *rightChild;
};


#endif
