import java.util.Scanner;

/**
 * Created by slandau on 1/11/17.
 */
public class IntegerPalindrome {

    public static boolean palindrome(long input) {
        // The reversed integer
        long reversed = 0;
        // A temporary variable for the input
        long temp = input;

        // Reverse the input and store it in the reversed variable
        while (temp != 0) {
            reversed *= 10; // multiply reversed by 10 so that we can add a new
            // integer to the end of it without it affecting the entire number
            reversed += temp % 10; // Get the last number of the input
            temp /= 10; // remove the last number of the input (temporary number)
        }

        return reversed == input;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long input = in.nextLong();
        System.out.println(palindrome(input));
    }
}
