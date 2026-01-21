import java.lang.Integer;
import java.lang.String;
import java.util.Scanner;

/**
 * @author zmiller
 */
public abstract class YOP {
    
    protected int[] csvToIntArray(String csv) {
        String[] strings = csv.split(",");
        int[] ints = new int[strings.length];
        for (int i = 0; i < strings.length; i++) {
            ints[i] = Integer.parseInt(strings[i].trim());
        }

        return ints;
    }

    /**
     * Executes the life cycle of the solution.
     * 
     * @param yop - class to execute 
     */
    protected static void launch(YOP yop) {
        
        String input;
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Type 'done' to terminate.\n");
        while(true) {
            System.out.print("Input: ");
            input = scan.nextLine();
            if(input.toLowerCase().equals("done")) {
                return;
            }
            
            yop.run(input);
        }
    }
    
    /**
     * Executes the solution
     * 
     * @param input - command line input
     */
    protected abstract void run(String input);
    
}
