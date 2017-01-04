import java.util.HashSet;

public class Main {

    // O(n) time, O(1) space hashing method
    public static char findTheDifference(String s, String t){
        if((s == null && t == null) || (s.length() == 0 && t.length() == 0)) return ' ';
        
        long diff = Math.abs(getHashValue(s) - getHashValue(t));
        return (char)(diff + 'a');
    }

    private static long getHashValue(String toHash){
        long hash = 0;
        for(char c : toHash.toCharArray()){
            hash += (long)c - 'a';
        }

        return hash;
    }
    
    // O(n) time, O(n) space Hash Set Method
    public static char findTheDifferenceHashSet(String s, String t){
      if((s == null && t == null) || (s.length() == 0 && t.length() == 0)) return ' ';
      
      HashSet<Character> set = new HashSet<Character>();
      
      for(char c : s.toCharArray()){
         if(set.contains(c)){
            set.remove(c);
         }else{
            set.add(c);
         }
      }
      
      for(char c : t.toCharArray()){
         if(set.contains(c)){
            set.remove(c);
         }else{
            set.add(c);
         }
      }
      
      return set.iterator().next();
    }
}