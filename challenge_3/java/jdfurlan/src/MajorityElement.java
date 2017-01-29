
import java.util.HashMap;

public class MajorityElement {

	public static void main(String[] args) {
		int[] nums = { 2, 2, 3, 7, 5, 7, 7, 7, 4, 7, 2, 7, 4, 5, 6, 7, 7, 8, 6, 7, 7, 8, 10, 12, 29, 30, 19, 10, 7, 7,
				7, 7, 7, 7, 7, 7, 7 };
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		for (int n : nums) {
			if (map.containsKey(n)) {
				int f = map.get(n) + 1;
				if (f > (nums.length / 2)) {
					System.out.println(n);
					System.exit(0);
				}
				map.put(n, f);
			} else {
				map.put(n, 1);
			}
		}

	}

}
