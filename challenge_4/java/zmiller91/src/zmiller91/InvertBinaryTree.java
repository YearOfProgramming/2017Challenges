/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zmiller91;

import java.util.LinkedList;

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
        
        // Stop when theres nothing to do
        if(root == null) {
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
        LinkedList<Node> q = new LinkedList<Node>();
        q.addLast(root);
        
        // Pop from the queue and add new nodes
        while(!q.isEmpty()) {
            
            // print the next node
            Node current = q.removeFirst();
            if(current.level() > level) {
                System.out.println();
                level = current.level();
            }
            System.out.print(current.value + " ");
            
            // Add the left node to the queue
            if(current.left() != null) {
                q.addLast(current.left());
            }
            
            // Add the right node to the queue
            if(current.right() != null) {
                q.addLast(current.right());
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