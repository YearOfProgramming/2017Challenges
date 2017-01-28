
public class FindTheMissingNumber {

	public static void main(String[] args) {
		int[] arr = { 6, 3, 4, 8, 1, 2, 0, 9, 10, 7 }; // missing is 5
		System.out.println(findMissingNum(arr));
	}

	private static int findMissingNum(int[] arr) {
		int actualSum = 0;
		int thisSum = 0;
		int i;
		for (i = 0; i < arr.length; i++) {
			actualSum += i+1;
			thisSum += arr[i];
		}
		return actualSum - thisSum;
	}

}
