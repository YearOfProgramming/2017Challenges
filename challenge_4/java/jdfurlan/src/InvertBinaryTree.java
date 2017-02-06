
import java.util.LinkedList;
import java.util.Queue;

public class InvertBinaryTree {

	public static void main(String[] args) {
		Node root = new Node(4);
		Node two = new Node(2);
		Node seven = new Node(7);
		Node three = new Node(3);
		Node six = new Node(6);
		Node nine = new Node(9);
		Node one = new Node(1);

		root.left = two;
		root.right = seven;
		two.left = one;
		two.right = three;
		seven.left = six;
		seven.right = nine;

		print(root);
		invertBT(root);
		System.out.println();
		print(root);


	}
	//breadth-first traversal using Queue interface
	private static void print(Node root) {
		Queue<Node> children = new LinkedList<Node>();
		children.add(root);
		while (!children.isEmpty()) {
			Node temp = children.poll();
			System.out.print(temp.data);
			if (temp.left != null)
				children.add(temp.left);
			if (temp.right != null)
				children.add(temp.right);
		}
	}
	//basic swap. Once swapped, swap left subtree then right subtree until null
	private static void invertBT(Node root) {
		if (root == null)
			return;
		Node temp = root.right;
		root.right = root.left;
		root.left = temp;
		invertBT(root.left);
		invertBT(root.right);
	}

}
