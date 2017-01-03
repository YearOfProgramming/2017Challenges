using System;

namespace Fojo
{
    public class Challenge1
    {
        public static void Main(string[] args)
        {
            //Not using linq :)
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
