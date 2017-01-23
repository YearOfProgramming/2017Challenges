using System;
namespace YOP2017
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a string to reverse: ");
            string input = Console.ReadLine();
            Console.WriteLine("Your string in reverse: " + Program.reverseString(input));
            Console.WriteLine("Press any key to exit.")
            Console.ReadKey(true);
        }
        public static string reverseString(string input)
        {
            char[] arr = input.ToCharArray();
            Array.Reverse(arr);
            return new string(arr);
        }
    }
}
