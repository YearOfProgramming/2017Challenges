import java.util.Scanner;

/**
 * This class holds the code needed to meet the requirements for Challenge 1 of
 * the 2017 Year of Programming.
 *
 * @author Jake Bashaw
 */
public class Challenge_1
{
    /**
     * Prints the reversed version of the standard input supplied by the user
     */
    public static void main(String args[])
    {
        System.out.print("> ");
        Scanner kb = new Scanner(System.in);
        String input = kb.nextLine();
        System.out.println(reverseString(input));
    }

    /**
     * Reverses and returns a String
     *
     * @param input The String to be reversed
     */
    public static String reverseString(String input)
    {
        StringBuilder sb = new StringBuilder(input);
        char forChar;
        char revChar;
        for(int i=0; i<sb.length()/2; i++)
        {
            forChar = sb.charAt(i);
            revChar = sb.charAt(sb.length()-i-1);
            sb.setCharAt(i, revChar);
            sb.setCharAt(sb.length()-i-1, forChar);
        }
        return sb.toString();
    }
}
