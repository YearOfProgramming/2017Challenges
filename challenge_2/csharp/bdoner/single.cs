using System;
using System.Linq;
using System.Collections.Generic;

class Single
{
    static void Main()
    {
        var array = new List<object> { 2, "a", "l", 3, "l", 4, "k", 2, 3, 4, "a", 6, "c", 4, "m", 6, "m", "k", 9, 10, 9, 8, 7, 8, 10, 7 };
        var dict = new Dictionary<object, bool>();
        foreach (var @char in array)
        {
            if (dict.ContainsKey(@char))
            {
                dict[@char] = true;
            }
            else
            {
                dict.Add(@char, false);
            }
        }
        Console.WriteLine(dict.FirstOrDefault(kvp => !kvp.Value).Key.ToString());
    }
}