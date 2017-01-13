using System;
using System.Linq;
using System.Collections.Generic;

namespace Challenge_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, bool> dic = new Dictionary<string, bool>();
            foreach(string el in args)
            {
                if(dic.ContainsKey(el))
                {
                    dic[el] = false;
                }
                else
                {
                    dic[el] = true;
                }
            }
            Console.WriteLine(dic.First((el) => el.Value).Key);
        }
    }
}