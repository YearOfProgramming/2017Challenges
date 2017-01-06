import java.util.List;
import java.util.ArrayList;

class Ranges {

    /** Each element RangeList represents one continuous range. */
    List<RangeList<Integer>> ranges;
    int[] input;

    public Ranges(int[] arr) {
        input = new int[arr.length];
        System.arraycopy(arr, 0, input, 0, arr.length);
        ranges = new ArrayList<RangeList<Integer>>();
        this.separate();
    }

    /** Populates the RANGES with the input from INPUT. */
    public void separate() {
        if (input.length > 0) {
            int prev = input[0];
            ranges.add(new RangeList<Integer>());
            ranges.get(0).add(prev);
            for (int i = 1, rangeIndex = 0; i < input.length; i += 1) {
                int next = input[i];
                if (next == prev + 1) {
                    ranges.get(rangeIndex).add(next);
                } else {
                    ranges.add(new RangeList<Integer>());
                    rangeIndex += 1;
                }
                prev = next;
            }
        }
    }

    public List<RangeList<Integer>> getRanges() {
        return ranges;
    }

    public String[] toStringArr() {
        List<String> rangesStrL = new ArrayList<String>();
        for (RangeList rl: ranges) {
            String rep = rl.toString();
            if (rep != null) {
                rangesStrL.add(rep);
            }
        }

        return rangesStrL.toArray(new String[0]);
    }
}
