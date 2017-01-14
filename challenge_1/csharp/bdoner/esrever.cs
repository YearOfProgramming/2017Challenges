using System;

class Reverse {

    static void Main() {
        var hello = "Hello!";
        for(var i = hello.Length - 1; i >= 0; i--) {
            Console.Write(hello[i]);
        }
    }
}