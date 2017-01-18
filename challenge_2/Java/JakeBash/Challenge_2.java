import java.io.*;
import java.util.*;
import java.util.Scanner;

/**
 * This class holds the code needed to meet the requirements for Challenge 2 of
 * the 2017 Year of Programming.
 *
 * @author Jake Bashaw
 */
public class Challenge_2
{
    /**
     * Prompts the user for input and displays the non-repeated string from the
     * input
     */
    public static void main(String[] args)
    {
        System.out.println("Please enter a series of space seperated characters");
        Scanner kb = new Scanner(System.in);
        String[] input = kb.nextLine().split(" ");
        System.out.println(singleNumber(input));
    }

    /**
     * Finds the only non-repeated String in an array of Strings
     *
     * @param input The String array that is to be searched
     */
    public static String singleNumber(String[] input)
    {
        HashMap<String, Integer> inputMap = new HashMap<>();

        for(String str : input)
        {
            if(inputMap.containsKey(str))
            {
                int value = inputMap.get(str);
                inputMap.remove(str);
                inputMap.put(str, value+1);
            }
            else
            {
                inputMap.put(str, 1);
            }
        }

        for (Map.Entry<String, Integer> entry : inputMap.entrySet())
        {
            String key = entry.getKey();
            int value = entry.getValue();

            if(value == 1)
            {
                return key;
            }
        }

        // If there are no non repeating elements
        return "No non-repeating elements were in the array";
    }
}
