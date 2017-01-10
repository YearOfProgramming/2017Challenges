package zmiller91;

import java.util.ArrayList;
import java.util.Collections;

/**
 * @author zmiller
 */
public class Squares {
    
    /**
     * Takes a sorted integer array and returns an array containing each 
     * elements square, in sorted order.
     * 
     * @param integers - array to square
     * @return - squared array
     */
    public static ArrayList<Double> square(int[] integers) {
        
        // Create a positive and negative array.
        ArrayList<Double> positives = new ArrayList<>();
        ArrayList<Double> negatives = new ArrayList<>();
        for(int i : integers) {
            Double squared = Math.pow(i, 2);
            if(i < 0) {
                negatives.add(squared);
            }
            else {
                positives.add(squared);
            }
        }
        
        // Since the input array is sorted the negatives array will have the 
        // largest absolute value first, reverse it so it can easily be merge sorted.
        Collections.reverse(negatives);
        
        // Merge sort
        ArrayList<Double> result = new ArrayList<>();
        int positiveIdx = 0;
        int negativeIdx = 0;
        
        while(positiveIdx < positives.size() || negativeIdx < negatives.size()) {
            
            Double p = positiveIdx < positives.size() ? 
                    positives.get(positiveIdx) : Double.MAX_VALUE;
            
            Double n = negativeIdx < negatives.size() ? 
                    negatives.get(negativeIdx) : Double.MAX_VALUE;
            
            if(p < n) {
                result.add(p);
                positiveIdx++;
            }
            else {
                result.add(n);
                negativeIdx++;
            }
        }
        
        return result;
    }
    
    /**
     * Method for testing equality.
     * 
     * @param expected
     * @param actual
     * @param message 
     */
    public static void assertEquals(Double[] expected, 
            ArrayList<Double> actual, String message) {
        
        if(expected.length != actual.size()) {
            throw new AssertionError(message);
        }
        
        for(int i = 0; i < expected.length; i++) {
            if(!expected[i].equals(actual.get(i))) {
                throw new AssertionError(message);
            }
        }
    }
    
    public static void main(String[] args) {
        
        // #1. The provided example
        int[] input = new int[]{-2, -1, 0, 1 ,2};
        assertEquals(new Double[]{0.0, 1.0, 1.0, 4.0, 4.0}, 
                square(input), "Test case 1 failed.");
        
        // #2. Uneven lists
        input = new int[]{-2, -1, 0, 2};
        assertEquals(new Double[]{0.0, 1.0, 4.0, 4.0}, 
                square(input), "Test case 2 failed.");
        
        // #3. One element
        input = new int[]{-2};
        assertEquals(new Double[]{4.0}, 
                square(input), "Test case 3 failed.");
        
        // #4. Same values
        input = new int[]{-2, 2};
        assertEquals(new Double[]{4.0, 4.0}, 
                square(input), "Test case 4 failed.");
        
        // #5. Empty list
        input = new int[]{};
        assertEquals(new Double[]{}, 
                square(input), "Test case 5 failed.");
        
        // #6. All negatives
        input = new int[]{-3, -2, -1};
        assertEquals(new Double[]{1.0, 4.0, 9.0}, 
                square(input), "Test case 6 failed.");
    }
    
}
