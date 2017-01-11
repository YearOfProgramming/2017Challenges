import java.lang.Integer;

/**
 * @author zmiller
 */


class Node {

	public int data;
	public Node left;
	public Node right;

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
			return head.left;
		}

		if (data > head.data) {
			if (head.right != null) {
				return insert(data, head.right);
			} 

			head.right = new Node(data);
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
		remove(search(data, n), n, n);
	}

	/**
	* Removes an element from the list; `n` will remain the head
	* after removal;
	*
	* @param data - value to delete
	* @param n - head of subtree
	* @param head - a reference to the head of the tree
	*/
	private void remove(Node remove, Node n, Node head) {

		// Find the node
		if (remove == null){
			return;
		}

		// Find the minimum element on the right.
		if (remove.right != null) {

				// The smallest can't have a left, if it has a
				// right then shift it up
				Node smallest = smallest(remove.right);
				swap(smallest, remove);
				remove(smallest, remove, head);
		}

		// Find the largest element on the left. 
		else if(remove.left != null) {

			    // The largest can't have a right, if it has a
				// left then shift it up
				Node largest = largest(remove.left);
				swap(largest, remove);
				remove(largest, remove, head);
		}

		else {

			System.out.println("pruning...");
			// Has neither
			prune(remove, head);
		}
	}

	/**
	* Prints a tree in preorder DFS. 
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
	* Finds the smalles element in a BST
	* 
	* @param n - root of the tree
	* @return the smallest node in the tree
	*/
	private Node smallest(Node n) {

		if (n == null) {
			return null;
		}

		while (n.left != null) {
			n = n.left;
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

		if (n == null) {
			return null;
		}

		while (n.right != null) {
			n = n.right;
		}

		return n;
	}

	/**
	* Prunes a tree be removing `data` and it's
	* subtree.
	*
	* @param data - node to prune
	* @param head of the tree
	*/
	private void prune(Node prune, Node head) {

		if (prune == null || head == null || prune == head) {
			return;
		}


		System.out.println("------");
		System.out.println(prune.data);
		System.out.println(head.data);
		System.out.println("------");

		if(prune.data < head.data && head.left != null) {
			if(head.left.data == prune.data) {
				head.left = null;
				return;
			}

			prune(prune, head.left);
		}

		if(prune.data > head.data && head.right != null) {
			if(head.right.data == prune.data) {
				head.right = null;
				return;
			}

			prune(prune, head.right);
		}
	}

	/**
	* Swaps the two objects
	*
	* @param a - first node
	* @param b - second node
	*/
	private void swap(Node a, Node b) {

		int temp = a.data;
		a.data = b.data;
		b.data = temp;
	}

    /**
     * Executes the problem's solution
     * 
     * @param input 
     */
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