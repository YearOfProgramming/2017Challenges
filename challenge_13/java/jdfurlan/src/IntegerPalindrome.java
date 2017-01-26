import java.util.Scanner;

public class IntegerPalindrome {

	/**
	 * 
	 * @param i, integer to check if palindrome
	 * @return boolean
	 */
	private static boolean checkPal(int i) {
		int original = i;
		int rev = 0;
		while (i > 0) {
			//order of operations is important here. assignments have the lowest
			//precedence, so the * happens first, then the i % 10, then the addition, then assignment
			rev = rev * 10 + i % 10;
			i /= 10;//chop off the last digit
		}
		return rev == original;//compare our reversed num with the original
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			System.out.println("Enter a positive integer value to check if palindrome, or 'exit' to quit: ");
			String num = sc.next();
			if (num.equals("exit"))
				System.exit(0);
			try {
				System.out.println(checkPal(Integer.valueOf(num)));
			} catch (NumberFormatException e) {
				System.out.println("Invalid input.");
			}
		}
	}
}
