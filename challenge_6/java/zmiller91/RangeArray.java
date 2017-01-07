
import java.util.ArrayList;

/**
 * @author zmiller
 */
public class RangeArray {
    
    public static ArrayList<String> findRange(int[] input) {
        
        // Fill the range arrays
        ArrayList<Integer> starts = new ArrayList<>();
        ArrayList<Integer> ends = new ArrayList<>();
        
        int expected = input[0];
        starts.add(expected);
        for(int i : input) {
            if(i != expected) {
                ends.add(expected - 1);
                starts.add(i);
            }
            
            expected = i + 1;
        }
        
        ends.add(input[input.length - 1]);
        
        // Construct the solution
        ArrayList<String> retval = new ArrayList<>();
        for(int i = 0; i < starts.size(); i++) {
            if(starts.get(i).equals(ends.get(i))) {
                continue;
            }
            retval.add(starts.get(i) + "->" + ends.get(i));
        }
        
        return retval;
    }
    
    public static void main(String[] args) {
        
        // Input
        int[] input = new int[]{1,2,3,4,8,9,10,12,13,14};
        ArrayList<String> solution = findRange(input);
        for(String s : solution){
            System.out.println(s);
        }
    }
}
