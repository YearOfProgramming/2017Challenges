/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zmiller91;

import java.util.HashSet;

/**
 *
 * @author zmiller
 */
public class SingleNumber {
    
    public static void main(String[] args) {
        
        // Input
        String[] input = new String[]{"2","a","l","3","l","4","k","2","3","4",
            "a","6","c","4","m","6","m","k","9","10","9","8","7","8","10","7"};
        
        HashSet<String> singles = new HashSet<String>();
        HashSet<String> found = new HashSet<String>();
        for(String s : input){
            
            // Found before, remove from singles set
            if (found.contains(s)) {
                singles.remove(s);
            }
            
            // Not found before, add to all and singles set
            else {
                found.add(s);
                singles.add(s);
            }
        }
        
        // The answer is whatever's left in the singles set
        for(String s : singles) {
            System.out.println(s);
        }
    }
}
