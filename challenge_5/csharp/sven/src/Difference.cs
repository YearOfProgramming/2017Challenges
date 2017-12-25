using System;
using System.Linq;
using System.Collections.Generic;

namespace Challenge_5
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(args[1].Except(args[0]).First());
        }
    }
}