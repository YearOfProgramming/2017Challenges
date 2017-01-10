import java.util.Arrays;
import java.util.List;
import java.util.Stack;

/**
 * @author zmiller
 */
public class ValidClosers extends YOP {
    
    private final String FALSE = "false";
    private final String TRUE = "true";
    private final List<Character> openers = Arrays.asList('{', '[', '(');
    private final List<Character> closers = Arrays.asList('}', ']', ')');
    
    /**
     * Validates that the given input has a correct sequence of openers and 
     * closers
     * 
     * @param input 
     */
    protected void run(String input) {
        
        Stack<Character> stack = new Stack<>();
        for(char c : input.toCharArray()) {
            
            // No rules for openers, add it to the stack
            if (openers.contains(c)) {
                stack.push(c);
            }
            
            // Openers have a few rules
            if (closers.contains(c)) {
                
                // Stack cannot be empty
                if(stack.empty()) {
                    System.out.println(FALSE);
                    return;
                }
                
                // The last element pushed must be an opener
                int openerIdx = openers.indexOf(stack.pop());
                if(openerIdx == -1) {
                    System.out.println(FALSE);
                    return;
                }
                
                // The opener and closer must match
                Character expected = closers.get(openerIdx);
                if (!expected.equals(c)) {
                    System.out.println(FALSE);
                    return;
                }
            }
        }
        
        // Stack must be empty
        if (stack.size() != 0) {
            System.out.println(FALSE);
            return;
        }
        
        System.out.println(TRUE);
    }
    
    public static void main(String args[]) {
        launch(new ValidClosers());
    }
}
