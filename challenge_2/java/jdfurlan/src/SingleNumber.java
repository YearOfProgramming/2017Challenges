
import java.util.HashMap;

public class SingleNumber {

	public static void main(String[] args) {
		String[] arr = { "2", "a", "l", "3", "l", "4", "k", "2", "3", "4", "a", "6", "c", "4", "m", "6", "m", "k", "9",
				"10", "9", "8", "7", "8", "10", "7" };
		HashMap<String, Integer> map = new HashMap<String, Integer>();
		for (String s : arr) {
			if (map.containsKey(s)) {
				map.put(s, map.get(s) + 1);
			} else {
				map.put(s, 1);
			}
		}
		for (String s : map.keySet()) {
			if (map.get(s) == 1) {
				System.out.println(s);
				System.exit(0);
			}
		}
	}

}
