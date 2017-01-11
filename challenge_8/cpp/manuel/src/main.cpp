#include <iostream>
#include <string>

#include "include/tools.h"
#include "include/LinkedList.h"

int main(int argc, char **argv) {

    LinkedList list;
    list.insert("hello");
    std::cout << list.data() << std::endl;

    return 0;
}
