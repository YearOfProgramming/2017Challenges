
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Random;
/**
 * 
 * @author jesse furlan
 * 
 * THIS CODE IS INCOMPLETE
 * This is simply my best effort to finish this challenge
 * Logic error with assigning the nodes randomly. Will come back to this 
 * challenge at a later time.
 *
 */
public class RandomPointerLinkedList {
	public static void main(String[] args) {
		ArrayList<ListNode> listNodes = new ArrayList<ListNode>();
		ArrayList<String> data = new ArrayList<String>();
		ListNode fifth = new ListNode("5", null, null);
		ListNode fourth = new ListNode("4", fifth, null);
		ListNode third = new ListNode("3", fourth, null);
		ListNode second = new ListNode("2", third, null);
		ListNode first = new ListNode("1", second, null);
		listNodes.add(first);
		listNodes.add(second);
		listNodes.add(third);
		listNodes.add(fourth);
		listNodes.add(fifth);
		HashMap<String, ListNode> map = new HashMap<String, ListNode>();
		for(ListNode n : listNodes){
			data.add(n.data);
			map.put(n.data, n);
		}
		genRandomNodes(listNodes,map,data);
	}

	private static ArrayList<ListNode> genRandomNodes(ArrayList<ListNode> listNodes, HashMap map, ArrayList<String> data) {
		Random r = new Random();
		
		for(ListNode node : listNodes){
			int idx = r.nextInt(data.size());
			node.random = (ListNode) map.get(data.get(idx));
			data.remove(idx);			
		}
		return null;
	}

}

class ListNode {
	ListNode next;
	ListNode random;
	String data;

	public ListNode(String data, ListNode next, ListNode random) {
		this.next = next;
		this.random = random;
		this.data = data;

	}
}
