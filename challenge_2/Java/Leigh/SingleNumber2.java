
import java.util.ArrayList;

public class SingleNumber {
    public static void main (String... args) {
        String[] list = new String[] {
            "2", "3", "4", "2", "3", "5", "4", "6", "4", 
            "6", "9", "10", "9", "8", "7", "8", "10", "7"
        };
        String[] list2 = new String[] {
            "2", "a", "l", "3", "l", "4", "k", "2", "3", 
            "4", "a", "6", "c", "4", "m", "6", "m", "k", 
            "9", "10", "9", "8", "7", "8", "10", "7"
        };

        System.out.println(findUniqueChar(list));  // 5
        System.out.println(findUniqueChar(list2)); // c
    }

    public static String findUniqueChar (String[] list) {
        ArrayList<String> chars         = new ArrayList<String>();
        ArrayList<String> charsToRemove = new ArrayList<String>();

        for (int i = 0; i < list.length; i++) {
            if (chars.contains(list[i])) {
                chars.add(list[i]);
                charsToRemove.add(list[i]);
            } else {
                chars.add(list[i]);
            }
        }

        return uniqueChar(chars, charsToRemove);
    }

    // Remove non-unique chars.
    public static String uniqueChar (ArrayList<String> uniqueChars, 
                                   ArrayList<String> charsToRemove) {
        uniqueChars.removeAll(charsToRemove);

        return uniqueChars.get(0);
    }
}
