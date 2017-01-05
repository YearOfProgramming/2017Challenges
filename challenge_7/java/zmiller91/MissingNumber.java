/**
 * @author zmiller
 */
public class MissingNumber {
    
    public static int find(int[] input) {
        
        // Invalid
        if (input.length <= 1) {
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
        int sumZeroToMin = (min - 1) * (min) / 2;
        int sumZeroToMax = max * (max + 1) / 2;
        int expectedSum = sumZeroToMax - sumZeroToMin;
        
        // The answer is the difference between the expected and actual
        int difference = expectedSum - actualSum;
        return  difference != 0 ? difference : -1;
    }
    
    public static void main(String[] args) {
        
        int[] input = new int[]{9, 7, 5, 8};
        System.out.println(find(input));
    }
}
