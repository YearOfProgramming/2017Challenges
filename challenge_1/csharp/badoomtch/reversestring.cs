using System;

namespace ProgrammingPlayground
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Input any string here ");
            string input = Console.ReadLine();
            char[] inputarray = input.ToCharArray();
            Array.Reverse(inputarray);
            string output = new string(inputarray);
            Console.WriteLine(output);
            Console.ReadLine();
        }
    }
}



