using System;
using System.Linq;
using System.Collections.Generic;

namespace Challenge_3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(args.GroupBy(val => val).OrderBy(g => g.Count()).Last().Key);
        }
    }
}