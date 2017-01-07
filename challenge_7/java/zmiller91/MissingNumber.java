/**
 * @author zmiller
 */
public class MissingNumber {
    
	/**
	 * Find the missing number in the provided array.
	 * 
	 * @param input - the array with a missing number
	 * @return the missing number
	 */
    public static int find(int[] input) {
        
        // Invalid
        if (input.length == 0) {
            return -1;
        }
        
        // Find the sum, min, and max values
        int actualSum = 0;
        for(int i : input) {
            actualSum += i;
        }
        
        // The answer is the difference between the expected and actual
        int N = input.length;
        int expectedSum = N * (N + 1) / 2;
        return expectedSum - actualSum;
    }
    
    public static void main(String[] args) {
        
    	// Should be 0
        int[] input = new int[]{1, 2, 3, 4};
        System.out.println(find(input));
        
        // Should be 4
        input = new int[]{0, 1, 2, 3};
        System.out.println(find(input));
        
        // Should be 2
        input = new int[]{0, 1, 4, 3};
        System.out.println(find(input));
        
        // Should be 0
        input = new int[]{1};
        System.out.println(find(input));
        
        // Should be -1
        input = new int[]{};
        System.out.println(find(input));
    }
}
