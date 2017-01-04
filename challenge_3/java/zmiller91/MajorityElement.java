
import java.util.Arrays;

/**
 *
 * @author zmiller
 */
public class MajorityElement {
    
    public static void main(String[] args) {
        
        int[] array = new int[]{2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,
            10,12,29,30,19,10,7,7,7,7,7,7,7,7,7};
        
        Arrays.sort(array);
        System.out.println(array[array.length/2]);
    }
    
}
