import java.util.List;
import java.util.ArrayList;

class FindTheDifference {
    ArrayList<Character> s;
    ArrayList<Character> t;

    public FindTheDifference(String s, String t) {
        this.s = new ArrayList<Character>();
        this.t = new ArrayList<Character>();
        for (int i = 0; i < s.length(); i += 1) {
            char k = s.charAt(i);
            this.s.add(k);
        }

        for (int i = 0; i < t.length(); i += 1) {
            char k = t.charAt(i);
            this.t.add(k);
        }
    }

    public void sortS() {

    }

    public void sortT() {

    }

    /** Sorts LST using quicksort.
     *  This function should be in a different class if you were to follow OOP principles.
     */
    public static char[] quicksort(char[] lst) {
        return null;
    }

    /** Find the appropriate pivot character in LST
     */
    public static double findPivot(List<Character> lst) {
        int sum = 0;
        for (char x: lst) {
            sum += x;
        }
        return sum/lst.size();
    }


}
