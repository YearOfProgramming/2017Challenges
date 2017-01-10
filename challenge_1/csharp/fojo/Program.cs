namespace Challenges
{
    public class Challenge1
    {
        public static string ReverseString(string inputString)
        {
            var reversedString = string.Empty;
            for (var i = inputString.Length - 1; i >= 0; i--)
            {
                reversedString += inputString[i];
            }
            return reversedString;
        }
    }
}
