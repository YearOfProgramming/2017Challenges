import java.lang.Math.*;

class FindTheDifference {
    char[] s;
    char[] t;

    public FindTheDifference(String s, String t) {
        this.s = new char[s.length()];
        this.t = new char[t.length()];
        for (int i = 0; i < s.length(); i += 1) {
            char k = s.charAt(i);
            this.s[i] = k;
        }

        for (int i = 0; i < t.length(); i += 1) {
            char k = t.charAt(i);
            this.t[i] = k;
        }
    }

    public void sortS() {

    }

    public void sortT() {

    }

    /** Sorts LST using quicksort.
     *  This function should be in a different class if you were to follow OOP principles.
     */
    public static void quicksort(char[] lst) {

    }

    /** Find the appropriate pivot character in LST
     */
    public static void findPivot(char[] lst) {

    }


}
