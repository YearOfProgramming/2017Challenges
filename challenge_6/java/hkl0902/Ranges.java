import java.util.List;
import java.util.ArrayList;

class Ranges {
    List<RangeList<Integer>> ranges;
    int[] input;

    public Ranges(int[] arr) {
        System.arraycopy(arr, 0, input, 0, arr.length);
        ranges = new ArrayList<RangeList<Integer>>();
    }
}
