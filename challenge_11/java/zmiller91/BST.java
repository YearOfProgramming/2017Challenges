import java.lang.Integer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author zmiller
 */
class Node {
    public int data;
    public Node left;
    public Node right;
    public Node parent;

    public Node(int data) {
        this.data = data;
    }
}

class BST extends YOP {

    /**
    * Returns the object containing the provided data point
    * 
    * @param data - value to be deleted
    * @param n - tree to look at
    */
    public Node search(int data, Node n) {

        // Not found
        if (n == null) {
                return null;
        }

        // Found, return the node
        if (data == n.data) {
                return n;
        }

        // Search the next tree
        Node next = data < n.data ? n.left : n.right;
        return search(data, next);
    }

    /**
    * Inserts a value into a BST.
    *
    * @param data - what to insert
    * @param head - where to insert
    * @return insert node
    */
    public Node insert (int data, Node head) {

        if (head == null) {
                return new Node(data);
        }

        if (data < head.data) {
            if (head.left != null) {
                return insert(data, head.left);
            } 

            head.left = new Node(data);
            head.left.parent = head;
            return head.left;
        }

        if (data > head.data) {
            if (head.right != null) {
                return insert(data, head.right);
            } 

            head.right = new Node(data);
            head.right.parent = head;
            return head.right;
        }

        // Ignore duplicates
        return null;
    } 

    /**
    * Removes an element from the list; `n` will remain the head
    * after removal;
    *
    * @param data - value to delete
    * @param n - head of subtree
    */
    public void remove(int data, Node n) {
        remove(search(data, n), n);
    }

    /**
    * Removes an element from the list; `n` will remain the head
    * after removal;
    *
    * @param data - value to delete
    * @param n - head of subtree
    * @param head - a reference to the head of the tree
    */
    public void remove(Node remove, Node n) {

        if (remove == null){
                return;
        }

        // Get the smallest on the right or largest on the left, depending on
        // what children are set
        Node swap = remove.right != null ? smallest(remove.right) : 
                remove.left != null ? largest(remove.left) : null;
        
        // Not a leaf node, recurse
        if (swap != null) { 
            remove.data = swap.data;
            remove(swap, remove);
        }
        
        // Leaf node, unset the reference
        else {
            Node parent = remove.parent;
            parent.left = parent.left != remove ? parent.left : null;
            parent.right = parent.right != remove ? parent.right : null;
        }
    }

    /**
    * Finds the smallest element in a BST
    * 
    * @param n - root of the tree
    * @return the smallest node in the tree
    */
    private Node smallest(Node n) {

        if (n != null) {
            while (n.left != null) {
                n = n.left;
            }
        }
        return n;
    }

    /**
    * Finds the largest element in a BST
    * 
    * @param n - root of the tree
    * @return the largest node in the tree
    */
    private Node largest(Node n) {

        if (n != null) {
            while (n.right != null) {
                n = n.right;
            }
        }
        
        return n;
    }

    /**
    * Prints a tree in pre-order DFS. 
    *
    * @param head - tree to print
    */
    public void print(Node head) {

        if (head == null) {
            return;
        }

        System.out.println(head.data);
        print(head.left);
        print(head.right);
    }

    /**
     * Executes the problem's solution
     * 
     * @param input 
     */
    @Override
    protected void run(String input) {

    	// Create the BST
    	String[] split = input.split("\\|");
    	int remove = Integer.parseInt(split[1].trim());
    	Node head = null;
    	for (int i : csvToIntArray(split[0])) { 
            if (head == null) {
                head = new Node(i);
                continue;
            }

            insert(i, head);
    	}

    	print(head);
    	remove(remove, head);
    	System.out.println();
    	print(head);
    }
    
    public static void main(String args[]) {
        launch(new BST());
    }
}