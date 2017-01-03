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
public class InvertBinaryTree {
    
    /**
     * Post order tree traversal to invert the tree from the bottom up.
     * 
     * @param root - binary tree
     */
    public static void invert(Node root) {
        
        // Stop at the n-1 row
        if(root.left() == null && root.right() == null) {
            return;
        }
        
        // Recurse over the left and right subtrees
        invert(root.left());
        invert(root.right());
        
        // Invert during post-processing
        root.addEdges(root.right(), root.left());
    }
    
    /**
     * Prints a binary tree from top to bottom via BFS
     * 
     * @param root
     */
    public static void print(Node root) {
        
        int level = root.level();
        
        // Create the node queue and enqueue the first value
        Queue<Node> q = new Queue<Node>();
        q.enqueue(root);
        
        // Pop from the queue and add new nodes
        while(!q.empty()) {
            
            // print the next node
            Node current = q.dequeue();
            if(current.level() > level) {
                System.out.println();
                level = current.level();
            }
            System.out.print(current.value + " ");
            
            // Add the left node to the queue
            if(current.left() != null) {
                q.enqueue(current.left());
            }
            
            // Add the right node to the queue
            if(current.right() != null) {
                q.enqueue(current.right());
            }
        }
        
        System.out.println();
    }
    
    /**
     * Main method for execution. This method will print the tree before
     * inversion and after inversion. It the tree defined in the problem
     * statement.
     * 
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Node four = new Node(4);
        Node two = new Node(2);
        Node seven = new Node(7);
        Node one = new Node(1);
        Node three = new Node(3);
        Node six = new Node(6);
        Node nine = new Node(9);
        
        four.addEdges(two, seven);
        two.addEdges(one, three);
        seven.addEdges(six, nine);
        
        System.out.println("Before Inversion");
        print(four);
        invert(four);
        
        System.out.println("\nAfter Inversion");
        print(four);
    }
}