using System;
using System.Linq;
using System.Collections.Generic;

namespace Challenge_5
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> list = args.Select(arg => int.Parse(arg)).ToList();
            int rangeBegin = list.First();
            int rangeEnd = rangeBegin;

            for (int i = 1; i < list.Count; i++)
            {
                if (rangeEnd + 1 == list[i])
                {
                    rangeEnd++;
                }
                else
                {
                    Console.WriteLine(rangeBegin + "->" + rangeEnd);
                    rangeBegin = list[i];
                    rangeEnd = rangeBegin;
                }
            }
            Console.WriteLine(rangeBegin + "->" + rangeEnd);
        }
    }
}