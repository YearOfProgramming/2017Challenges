
public class Test {
    // swaps array elements i and j
    public static void exchange(char[] a, int i, int j) {
        char temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    // returns a random integer between 0 and n-1
    public static int uniform(int n) {
        return (int) (Math.random() * n);
    }

    // take as input an array of strings and rearrange them in random order
    public static String shuffle(char[] a) {
        int n = a.length;
        for (int i = 0; i < n; i++) {
            int r = i + uniform(n-i);   // between i and n-1
            exchange(a, i, r);
        }
        
        return new String(a);
    }

    public static void main(String[] args) {
        long t1, t2;
        String answer;
        char result;
        
        //As the first test, this always takes longer to run than others of comparable length
        //Short String timing
        System.out.println("Short String");
        String s = "abcd";
        String t = s + "e";
        t = shuffle(t.toCharArray());
        
        t1 = System.currentTimeMillis();
        result = Main.findTheDifference(s,t);
        t2 = System.currentTimeMillis();
        answer = (result == 'e')? "Correct" : "Incorrect";
        System.out.println("Your solution took " + (t2-t1) + "ms to complete.");
        System.out.println("Your answer was: " + answer);
        
        //Medium String timing
        System.out.println("\nMedium String");
        s = "abcdefghijklmno";
        t = s + "p";
        t = shuffle(t.toCharArray());
        
        t1 = System.currentTimeMillis();
        result = Main.findTheDifference(s,t);
        t2 = System.currentTimeMillis();
        answer = (result == 'p')? "Correct" : "Incorrect";
        System.out.println("Your solution took " + (t2-t1) + "ms to complete.");
        System.out.println("Your answer was: " + answer);
        
        //Empty String timing
        System.out.println("\nEmpty String");
        
        t1 = System.currentTimeMillis();
        result = Main.findTheDifference("","");
        t2 = System.currentTimeMillis();
        answer = (result == ' ')? "Correct" : "Incorrect";
        System.out.println("Your solution took " + (t2-t1) + "ms to complete.");
        System.out.println("Your answer was: " + answer);
        
        //Long String timing
        System.out.println("\nVery long String");
        s = "yipsqffxmqafnrlnkwrnvspeekejbsuuvuhanlxmgkyjlgmloxmpyxuvqeabmycqycwkzvhyviaavwryyhtepqacfuzggcoctviibhbcwzmkbsivtjywienaojkcekvgsyylliasczuzoivipcsqknbshavzwyufkeaxjiunbyiuvxvpfokrfphcxbaljktkiygrboihqczhxnreigzhsinustzzrzstbpkfrqsenhrnkrfbekfwaozenxqabbhhsaxyrubmtzmvtclatncfkkvplvuwzfggfnprinyjblutbovtmxxvacouiwgrkgjvszkwswvnwaggsiwzymixwmhmujmuckgyiwcwrigtshqeuguytpjjsrmijmxikeraqqgjymbvmvcugxubuxmlzoiqzfjwpzpqnwalcxczzxaitpmjsorwzmwzgjcgpztaynujqqmhvyscupqjflrnjqseeapavmakvexuvkntgcvkvonjqoivimybahutpjtzubamihhbyhspgtmjwexylkqqjvmtpxxcjnlpbkaiiekjlxkrewthipzhfljcfyuclowlptfhksrngxpzijabhfjhwtlbfuouqskheybgoqinmhnjzciqvscvneokfqrghekuzkahlyosemcgqipimjaypxkkwvtqztcexlhogjqfxvfihqqcriaimioaezfrbaxwfuwbiylpztmxovutxwhqrlrxfwpfcppazjsztewupvarsqcizlneiomljrbufbuhljmgnlqkofsersqhfucsvfswqxnmqlthjcopeaseqmsghvqpnmxmuvuoteoqsaneknirsjrleslfsiceoypypbijhmtmesxpxcurnxjzwjclcesyfmffbcsxvnlhtnmwgxaywahyhqqfuevmwhhovxrqsslemlpxeiuqipmtqmeqosghyvgyexblvmsbofvtjqfhcowmfvhyyerktinhggqamtykvntxyywn";
        t = s + "p";
        t = shuffle(t.toCharArray());
         
        t1 = System.currentTimeMillis();
        result = Main.findTheDifference(s,t);
        t2 = System.currentTimeMillis();
        answer = (result == 'p')? "Correct" : "Incorrect";
        System.out.println("Your comstant space solution took " + (t2-t1) + "ms to complete.");
        System.out.println("Your answer was: " + answer);
        
        t1 = System.currentTimeMillis();
        result = Main.findTheDifferenceHashSet(s,t);
        t2 = System.currentTimeMillis();
        answer = (result == 'p')? "Correct" : "Incorrect";
        System.out.println("Your hashset solution took " + (t2-t1) + "ms to complete.");
        System.out.println("Your answer was: " + answer);
        
    }
}
