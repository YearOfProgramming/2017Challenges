public class Reversal {
	public static void main(String[] args) {
		System.out.println(reverse(args[0]));
	}
	
	private static String reverse(String input) {
		String reversed = "";
		for(int i = 0; i<input.length(); i++)
			reversed += input.charAt(input.length() - i - 1);
		return reversed;
	}
}