// NOTE_TO_FUTURE_SMARTER_SELF: User generics.
// NOTE: This is a simple implementation.

import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class Histogram {
    private Map<String, Integer> histogram;

    public Histogram () {
        histogram = new HashMap<String, Integer>();
    }

    public boolean add (String item) {
        if (histogram.containsKey(item)) {
            histogram.replace(item, histogram.get(item) + 1);
            return false;
        } else histogram.put(item, 1);
        
        return true;
    }

    public boolean remove (String item) {
        if (histogram.containsKey(item)) 
            histogram.remove(item);
        else return false;
        
        return true;
    }
    
    public boolean contains (String item) {
        if(histogram.containsKey(item)) return true;
        return false;
    }

    public int getValue (String item) {
        if (histogram.containsKey(item)) 
            return histogram.get(item);
        
        return -1;
    }

    public ArrayList<String> keySet () {
        return new ArrayList<String>(histogram.keySet());
    }

    public ArrayList<Integer> values () {
        return new ArrayList<Integer>(histogram.values());
    }
}
