
import java.util.Scanner;

public class ReverseAString {

	public static void main(String[] args) {
		try(Scanner sc = new Scanner(System.in)){
			char[] input = sc.next().toCharArray();
		}
		int j = input.length - 1;
		for (int i = 0; i < input.length / 2; i++, j--) {
			char temp = input[j];
			input[j] = input[i];
			input[i] = temp;
		}
		System.out.println(String.valueOf(input));
	}
}
