
import java.util.ArrayList;

public class Ranges {

	public static void main(String[] args) {
		int[][] arr = { { 1, 2, 3, 4, 8, 9, 10, 12, 13, 14 }, { 1, 2, 3, 4, 9, 10, 15 }, { 1, 2 }, { 1 },
				{ 1, 2, 3, 4, 5, 8, 9, 10}, { 1, 3 }};
		for(int[] a : arr){
			System.out.println(findRanges(a));
		}
	}

	private static ArrayList<String> findRanges(int[] arr) {
		ArrayList<String> res = new ArrayList<String>();
		int first, last;
		for (int i = 0; i < arr.length - 1; i++) {
			first = arr[i];
			last = 0;
			while (i < arr.length-1 && arr[i + 1] == arr[i] + 1) {
				i++;
				last = arr[i];
			}
			if (last != 0)
				res.add(first + "->" + last);
		}
		return res;
	}

}
