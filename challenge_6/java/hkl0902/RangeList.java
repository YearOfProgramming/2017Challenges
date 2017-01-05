import java.util.List;
import java.util.ArrayList;

/**
 RangeList is a List of numbers in order that differ only by 1 and assumes that the user is using it correctly.
 A RangeList containing {1, 2, 4} would be invalid.
 A RangeList containing {1, 2, 3, 4} would be valid.
 A RangeList containing {1, 3, 2} would be invalid.
 */

class RangeList<T extends Integer> extends ArrayList<T> {
    /** Returns a string representation of RangeList.
     *  If the list contains {1, 2, 3}, it returns "1->3"
     *  If the list contains simply {1}, it returns "1"
     */
    @Override
    public String toString() {
        switch(this.size()) {
            case 0: return "";
            case 1: return "" + this.get(0);
            default: return this.get(0) + "->" + this.get(this.size() -1);
        }
    }
}
