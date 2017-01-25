
import java.util.ArrayList;

public class Squares {

	public static void main(String[] args) {
		int[] arr = {-9,4,9};

		ArrayList<Integer> myList = orderSquares(arr);
		for (int i : myList) {
			System.out.print(i + " ");
		}

	}

	private static ArrayList orderSquares(int[] arr) {
		ArrayList<Integer> result = new ArrayList<Integer>();
		ArrayList<Integer> negatives = new ArrayList<Integer>();
		ArrayList<Integer> positives = new ArrayList<Integer>();

		for (int i : arr) {
			if (i < 0) {
				negatives.add(0, i * i);
			} else {
				positives.add(i * i);
			}
		}
		int posIdx = 0;
		int negIdx = 0;

		while (posIdx < positives.size() || negIdx < negatives.size()) {

			int p = (posIdx < positives.size()) ? positives.get(posIdx) : Integer.MAX_VALUE;
			int n = (negIdx < negatives.size()) ? negatives.get(negIdx) : Integer.MAX_VALUE;

			if (p < n) {
				result.add(p);
				posIdx++;

			} else {
				result.add(n);
				negIdx++;

			}
		}

		return result;
	}

}
