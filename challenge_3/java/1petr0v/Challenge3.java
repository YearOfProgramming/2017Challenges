import java.util.List;
import java.util.Arrays;

public class Challenge3 {

    public static void main(String ... main) {
        MajorityElement<Integer> alg = new MajorityElementImpl();
        List<Integer> listOfInts = Arrays.asList(2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7);
        System.out.println(alg.findMajorObject(listOfInts));
    }

}
