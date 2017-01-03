package zmiller91;

/**
 * Nodes used for building a binary tree
 * 
 * @author zmiller
 */
public class Node {
    public int value;
    
    protected Node left;
    protected Node right;
    private int level;

    public Node(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
        level = 0;
    }
    
    /**
     * Getter for node level
     * 
     * @return 
     */
    public int level() {
        return level;
    }
    
    /**
     * Getter for left child node
     * 
     * @return 
     */
    public Node left() {
        return left;
    }
    
    /**
     * Getter for right child node
     * 
     * @return 
     */
    public Node right() {
        return right;
    }
    
    /**
     * Create edges to the left and right children
     * 
     * @param left - child node
     * @param right  - child node
     */
    public void addEdges(Node left, Node right) {
        
        this.left = left;
        if(left != null) {
            left.level = this.level + 1;
        }
        
        this.right = right;
        if(right != null) {
            right.level = this.level + 1;
        }
    }
}
