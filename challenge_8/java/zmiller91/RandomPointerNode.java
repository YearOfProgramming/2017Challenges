package zmiller91;

/**
 * Basic Node object to create a linked list
 * 
 * @author zmiller
 */
public class RandomPointerNode {
    
    public String data;
    public RandomPointerNode random;
    public RandomPointerNode next;
    
    public RandomPointerNode(String data) {
        this.data = data;
    }
}
