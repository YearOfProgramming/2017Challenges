using System;
using System.Linq;

namespace Challenge_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(
                args.Aggregate("", (sentence, word) => word.Aggregate("", (w, character) => character + w) + " " + sentence)
                );
        }
    }
}