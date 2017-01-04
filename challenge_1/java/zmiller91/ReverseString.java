/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zmiller91;

/**
 *
 * @author zmiller
 */
public class ReverseString {
    
    public static void main(String[] args){
        
        String input = "hello";
        StringBuilder sb = new StringBuilder(input);
        for(int i = 0; i < sb.length()/2; i++){
            char leftChar = sb.charAt(i);
            int rightIdx = sb.length() - 1 - i;
            sb.setCharAt(i, sb.charAt(rightIdx));
            sb.setCharAt(rightIdx, leftChar);
        }
        
        System.out.println(sb.toString());
    }
}
