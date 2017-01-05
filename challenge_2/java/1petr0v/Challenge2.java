import java.util.List;
import java.util.Arrays;

public class Challenge2 {

    public static void main(String ... main) {
        // Test 1.
        NotRepeatableAlgorithmImpl<Integer> algInt = new NotRepeatableAlgorithmImpl();
        List<Integer> listOfIntegers = Arrays.asList(2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7);
        algInt.findUniqueObjects(listOfIntegers).forEach(System.out::println);
        
        // Test 2.
        NotRepeatableAlgorithmImpl<Character> algChar = new NotRepeatableAlgorithmImpl();
        List<Character> listOfChars = Arrays.asList('2','a','l','3','l','4','k','2','3','4','a','6','c','4','m','6','m','k','9','1','9','8','7','8','1','7');
        algChar.findUniqueObjects(listOfChars).forEach(System.out::println);

    }

}
