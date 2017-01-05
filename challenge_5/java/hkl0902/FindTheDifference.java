import java.util.List;
import java.util.ArrayList;

class FindTheDifference {
    List<Character> s;
    List<Character> t;

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

    public char getTheDifference() {
        sortS();
        sortT();
        for (int i = 0; i < s.size(); i += 1) {
            if (s.get(i) != t.get(i)) {
                return t.get(i);
            }
        }
        return t.get(t.size() - 1);
    }

    public void sortS() {
        s = quicksort(s);
    }

    public void sortT() {
        t = quicksort(t);
    }

    /** Sorts LST using quicksort.
     *  This function should be in a different class if you were to follow OOP principles.
     */
    public static List<Character> quicksort(List<Character> lst) {
        if (lst.size() < 2) {
            return lst;
        }
        if (lst.size() < 3) {
            if (lst.get(0) < lst.get(1)) {
                return lst;
            }
            lst.add(0, lst.get(1));
            lst.remove(2);
            return lst;
        }
        double pivot = findPivot(lst);
        List<Character> left = new ArrayList<Character>();
        List<Character> right = new ArrayList<Character>();
        for (char k: lst) {
            if (k <= pivot) {
                left.add(k);
            } else {
                right.add(k);
            }
        }
        left = quicksort(left);
        right = quicksort(right);
        left.addAll(right);
        return left;

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
