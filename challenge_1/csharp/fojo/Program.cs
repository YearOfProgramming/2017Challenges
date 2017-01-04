using System;

namespace Fojo
{
    public class Challenge1
    {
        public static void Main(string[] args)
        {
            var inputString = Console.ReadLine();
            string reversedString = string.Empty;
            for (int i = inputString.Length - 1; i >= 0; i--)
            {
                reversedString += inputString[i];
            }
            Console.WriteLine(reversedString);
        }
    }
}
