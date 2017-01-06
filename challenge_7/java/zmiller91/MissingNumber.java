/**
 * @author zmiller
 */
public class MissingNumber {
    
    public static int find(int[] input) {
        
        // Invalid
        if (input.length == 0) {
            return -1;
        }
        
        // Find the sum, min, and max values
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        int actualSum = 0;
        for(int i : input) {
            actualSum += i;
            min = Math.min(min, i);
            max = Math.max(max, i);
        }
        
        // Calculate the expected sum
        int expectedSum = max * (max + 1) / 2;
        
        // The answer is the difference between the expected and actual
        return expectedSum - actualSum;
    }
    
    public static void main(String[] args) {
        
        int[] input = new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12};
        System.out.println(find(input));
    }
}
