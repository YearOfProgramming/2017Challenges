
import java.util.Arrays;

/**
 * @author zmiller
 */
public class Compression extends YOP{

    /**
     * Compresses a alphabetic string
     * 
     * @param input - string to compress
     * @return - compressed string
     */
    public String compress(String input) {
        
        StringBuilder retval = new StringBuilder();
        StringBuilder sequence = new StringBuilder();
        for(char c : input.toCharArray()) {

            // Found the end of a sequence
            if (sequence.length() > 0 && sequence.charAt(0) != c) {
                retval.append(formatForCompression(sequence));
                sequence = new StringBuilder();
            }
            
            // Add to the sequence
            sequence.append(c);
        }
        
        // Don't forget the leftovers
        return retval.append(formatForCompression(sequence)).toString();
    }
    
    /**
     * Decompresses an alphabetic string
     * 
     * @param input - string to decompress
     * @return  - decompressed string
     */
    public String decompress(String input) {
        StringBuilder retval = new StringBuilder();
        for(int i = 0; i < input.length(); i++) {
            
            // Compressed sequence, uncompress it
            if(input.charAt(i) == '#') {
                i++;
                
                // Find the number of repeated characters
                StringBuilder count = new StringBuilder();
                while(i < input.length() && isInt(input.charAt(i))) {
                    count.append(input.charAt(i));
                    i++;
                }
                
                // Append a string with the correct number of repeated characters
                retval.append(formatForDecompression(
                        retval.charAt(retval.length() - 1), 
                        Integer.parseInt(count.toString()) - 1));
                
                // Terminate if the string has been exhausted
                if(i == input.length()) {
                    break;
                }
            }
            
            retval.append(input.charAt(i));
        }
        
        return retval.toString();
    }
    
    /**
     * Checks if a character is an integer
     * 
     * @param i
     * @return 
     */
    private boolean isInt(char i) {
        try {
            Integer.parseInt(Character.toString(i));
            return true;
        }
        catch (Exception e) {
            return false;
        }
    }
    
    /**
     * Creates a string with repeated characters
     * 
     * @param fillWith - characters to repeat
     * @param size - number of repetitions
     * @return repeated character string
     */
    private String formatForDecompression(char fillWith, int size) {
        char[] chars = new char[size];
        Arrays.fill(chars, fillWith);
        return new String(chars);
    }
    
    /**
     * Takes a string with repeated characters and compresses it to the
     * proper format
     * 
     * @param sequence
     * @return 
     */
    private String formatForCompression(StringBuilder sequence) {
        if(sequence.length() > 3) {
            return Character.toString(sequence.charAt(0))+ "#" + 
                    Integer.toString(sequence.length());
        }
        
        return sequence.toString();
    }
    
    @Override
    protected void run(String input) {
        String compressed = compress(input);
        System.out.println("Compressed: " + compressed);
        String decompressed = decompress(compressed);
        System.out.println("Decompressed: " + decompressed);
        System.out.println("Decompressed == Input? " + decompressed.equals(input));
    }
    
    public static void main(String[] args) {
        launch(new Compression());
    }
}
