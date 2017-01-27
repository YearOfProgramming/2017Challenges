
import java.util.Scanner;

public class ReversingALinkedList {

	private static void printList(ListNode head) {
		while (head != null) {
			System.out.print(head.data);
			head = head.next;
		}
		System.out.println();
	}

	private static ListNode reverseList(ListNode current) {
		// create two helper nodes to track next node an previous node
		// initialize to null
		ListNode prev = null;
		ListNode next = null;
		while (current != null) {
			next = current.next;// capture the next node in the list
			current.next = prev;// reverse the link here
			// now we increment both previous and current nodes by "1"
			// the next node from previous is current
			prev = current;
			// the next node from current is next
			current = next;
		}
		return prev;
	}

	private static ListNode buildLinkedList(String word) {
		// if string is empty return null listNode
		if (word.length() <= 1)
			return new ListNode(null);
		// if string is length 2, that means one letter i.e. 'a '
		if (word.length() == 2)
			return new ListNode(String.valueOf(word.charAt(0)));
		String[] arr = word.split(" ");
		ListNode head = new ListNode(arr[0]);
		ListNode temp = head;// use temp to retain head
		for (int i = 1; i < arr.length; i++) {
			temp.next = new ListNode(arr[i]);
			temp = temp.next;// move through the list
		}

		return head;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			System.out.println("Enter a space separated word to be reversed, or 'exit': ");
			String word = sc.nextLine();
			if (word.equals("exit"))System.exit(0);
			ListNode forward = buildLinkedList(word);
			ListNode reversed = reverseList(buildLinkedList(word));
			printList(forward);
			printList(reversed);
		}

	}
}

class ListNode {
	String data;
	ListNode next;

	ListNode(String data) {
		this.data = data;
	}
}
