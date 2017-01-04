import java.util.Arrays;

public class MajorityElement {
    public static void main(String[] args){
        int testArr[] =  {2,2,3,7,5,7,7,7,4,7,2,7,4,5,6,7,7,8,6,7,7,8,10,12,29,30,19,10,7,7,7,7,7,7,7,7,7};
        System.out.println(majorityElement(testArr));    
    }

    public static int majorityElement(int[] arr) {
        //If an element is the majority element, then the middle item
        //will always be that element
        Arrays.sort(arr);
        return arr[arr.length / 2];
    }
}
