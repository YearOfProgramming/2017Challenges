using System;
using System.Linq;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // var array = new int[] { 2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7 };
            var array = new char[] { '2', 'a', 'l', '3', 'l','5', '4', 'k', '2', '3', '4', 'a', '6', 'c', '4', 'm', '6', 'm', 'k', '9', '0', '9', '8', '7', '8', '0', '7' };
            foreach (var x in array)
            {
                if (array.Where(y => y == x).Count() == 1)
                    Console.Write(x);
            }
        }
    }
}
