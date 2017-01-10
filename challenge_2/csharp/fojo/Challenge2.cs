using System.Collections.Generic;
using System.Linq;

namespace Challenges
{
    public class Challenge2
    {
        public static List<char> GetOneCountItems(char[] inputArray)
        {
            return inputArray.Where(x => inputArray.Count(i => i == x) == 1).ToList();
        }
    }
}
