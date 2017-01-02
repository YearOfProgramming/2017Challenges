#include <iostream>
#include <string>

int main(int argc, char **argv) {

    bool quit = false; // type "quit" to exit

    // keep reversing user input until user quits
    while(!quit) {

        std::string output;

        std::getline(std::cin, output); // grab user input

        // if user typed in "quit", then quit program
        quit = !std::string("quit").compare(output); 

        if (quit) {
            quit = true;
        }

        // print out in reverse
        for(int i = output.length() - 1; i >= 0; i--) {
            std::cout << output[i];
        }

        std::cout << std::endl;

    }


    return 0;
}
