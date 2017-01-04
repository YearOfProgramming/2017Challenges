
public class Test {
    public static void main(String[] args) {
        long t1, t2;
        String answer;
        char result;
        
        //Short String timing
        //As the first test, this always takes longer to run than others of comparable length
        System.out.println("Short String");
        
        t1 = System.currentTimeMillis();
        result = Main.findTheDifference("abcd","abcde");
        t2 = System.currentTimeMillis();
        answer = (result == 'e')? "Correct" : "Incorrect";
        System.out.println("Your solution took " + (t2-t1) + "ms to complete.");
        System.out.println("Your answer was: " + answer);
        
        //Short swapped String timing
        System.out.println("\nShort swapped String");
        
        t1 = System.currentTimeMillis();
        result = Main.findTheDifference("abcd","dcabe");
        t2 = System.currentTimeMillis();
        answer = (result == 'e')? "Correct" : "Incorrect";
        System.out.println("Your solution took " + (t2-t1) + "ms to complete.");
        System.out.println("Your answer was: " + answer);
        
        //Medium String timing
        System.out.println("\nMedium String");
        
        t1 = System.currentTimeMillis();
        result = Main.findTheDifference("abcdefghijklmno","abcdefghijklmnop");
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
        String s = "yipsqffxmqafnrlnkwrnvspeekejbsuuvuhanlxmgkyjlgmloxmpyxuvqeabmycqycwkzvhyviaavwryyhtepqacfuzggcoctviibhbcwzmkbsivtjywienaojkcekvgsyylliasczuzoivipcsqknbshavzwyufkeaxjiunbyiuvxvpfokrfphcxbaljktkiygrboihqczhxnreigzhsinustzzrzstbpkfrqsenhrnkrfbekfwaozenxqabbhhsaxyrubmtzmvtclatncfkkvplvuwzfggfnprinyjblutbovtmxxvacouiwgrkgjvszkwswvnwaggsiwzymixwmhmujmuckgyiwcwrigtshqeuguytpjjsrmijmxikeraqqgjymbvmvcugxubuxmlzoiqzfjwpzpqnwalcxczzxaitpmjsorwzmwzgjcgpztaynujqqmhvyscupqjflrnjqseeapavmakvexuvkntgcvkvonjqoivimybahutpjtzubamihhbyhspgtmjwexylkqqjvmtpxxcjnlpbkaiiekjlxkrewthipzhfljcfyuclowlptfhksrngxpzijabhfjhwtlbfuouqskheybgoqinmhnjzciqvscvneokfqrghekuzkahlyosemcgqipimjaypxkkwvtqztcexlhogjqfxvfihqqcriaimioaezfrbaxwfuwbiylpztmxovutxwhqrlrxfwpfcppazjsztewupvarsqcizlneiomljrbufbuhljmgnlqkofsersqhfucsvfswqxnmqlthjcopeaseqmsghvqpnmxmuvuoteoqsaneknirsjrleslfsiceoypypbijhmtmesxpxcurnxjzwjclcesyfmffbcsxvnlhtnmwgxaywahyhqqfuevmwhhovxrqsslemlpxeiuqipmtqmeqosghyvgyexblvmsbofvtjqfhcowmfvhyyerktinhggqamtykvntxyywn";
        String t = "yipsqffxmqafnrlnkwrnvspeekejbsuuvuhanlxmgkyjlgmloxmpyxuvqeabmycqycwkzvhyviaavwryyhtepqacfuzggcoctviibhbcwzmkbsivtjywienaojkcekvgsyylliasczuzoivipcsqknbshavzwyufkeaxjiunbyiuvxvpfokrfphcxbaljktkiygrboihqczhxnreigzhsinustzzrzstbpkfrqsenhrnkrfbekfwaozenxqabbhhsaxyrubmtzmvtclatncfkkvplvuwzfggfnprinyjblutbovtmxxvacouiwgrkgjvszkwswvnwaggsiwzymixwmhmujmuckgyiwcwrigtshqeuguytpjjsrmijmxikeraqqgjymbvmvcugxubuxmlzoiqzfjwpzpqnwalcxczzxaitpmjsorwzmwzgjcgpztaynujqqmhvyscupqjflrnjqseeapavmakvexuvkntgcvkvonjqoivimybahutpjtzubamihhbyhspgtmjwexylkqqjvmtpxxcjnlpbkaiiekjlxkrewthipzhfljcfyuclowlptfhksrngxpzijabhfjhwtlbfuouqskheybgoqinmhnjzciqvscvneokfqrghekuzkahlyosemcgqipimjaypxkkwvtqztcexlhogjqfxvfihqqcriaimioaezfrbaxwfuwbiylpztmxovutxwhqrlrxfwpfcppazjsztewupvarsqcizlneiomljrbufbuhljmgnlqkofsersqhfucsvfswqxnmqlthjcopeaseqmsghvqpnmxmuvuoteoqsaneknirsjrleslfsiceoypyppbijhmtmesxpxcurnxjzwjclcesyfmffbcsxvnlhtnmwgxaywahyhqqfuevmwhhovxrqsslemlpxeiuqipmtqmeqosghyvgyexblvmsbofvtjqfhcowmfvhyyerktinhggqamtykvntxyywn";
        
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
