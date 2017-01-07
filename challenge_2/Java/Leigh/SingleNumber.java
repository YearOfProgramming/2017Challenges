
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

    public static String findUniqueChar(String[] list) {
        Histogram histogram = new Histogram();

        for (String item : list) {
            histogram.add(item);
        }

        for (String item : histogram.keySet()) {
            if (histogram.getValue(item) == 1) return item;
        }

        return null;
    }
}
