import java.util.*;

public class SingleNumber {
    public static void main(String[] args) {
        int arr[] = {2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7};
        System.out.println(findSingleNumber(arr));
    }

    public static int findSingleNumber(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i : arr) {
            if(map.putIfAbsent(i, 1) != null) {
                map.put(i, map.get(i) + 1);
            }
        }
        
        for(Map.Entry<Integer, Integer> e : map.entrySet()) {
            if(e.getValue() < 2) {
                return e.getKey();
            }
        }
        return 0;
    }
}
