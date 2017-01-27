
public class FindTheDifference {

	public static void main(String[] args) {
		String s = "abcd";
		String t = "dbeca";

		boolean[] b = new boolean[128];
		for (int i = 0; i < s.length(); i++) {
			b[s.charAt(i)] = true;
		}
		for (int i = 0; i < t.length(); i++) {
			if (!b[t.charAt(i)]) {
				System.out.println(t.charAt(i) + " found at index: " + i);
				System.exit(0);
			}
		}
		System.out.println(t.charAt(0));
	}

}
