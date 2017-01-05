import java.util.List;
import java.util.ArrayList;

class Ranges {
    List<RangeList<Integer>> ranges;
    int rangeCount = 0;
    List<String> rangesStr;

    public Ranges(int[] arr) {
        ranges = new ArrayList<RangeList<Integer>>();
        if (arr.length > 0) {
            int prev = arr[0];
            ranges.add(new RangeList<Integer>());
            ranges.get(rangeCount).add(prev);
            for (int i = 1; i < arr.length; i += 1) {
                int next = arr[i];
                if (next == prev + 1) {
                    ranges.get(rangeCount).add(next);
                } else {
                    ranges.add(new RangeList<Integer>());
                    rangeCount += 1;
                }
                prev = next;
            }
        }
        rangesStr = new ArrayList<String>();
        for (int i = 0; i < rangeCount; i += 1) {
            rangesStr.add(ranges.get(i).toString());
            if (rangesStr.get(i) == null) {
                rangesStr.remove(i);
            }
        }
    }

    public int numofRanges() {
        return rangeCount;
    }

    public String[] rangesString() {
        return (String[])(rangesStr.toArray());
    }

}
