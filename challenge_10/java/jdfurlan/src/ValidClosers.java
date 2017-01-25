
import java.util.List;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Stack;
/**
 * 
 * @author jdfurlan but zmiller91's comments and solution helped immensely!
 *
 */
public class ValidClosers {

	private static boolean checkClosers(String nextLine) {
		if (nextLine.length() == 0)
			return true;
		List<Character> openers = Arrays.asList('{', '[', '(');
		List<Character> closers = Arrays.asList('}', ']', ')');
		Stack<Character> stack = new Stack<Character>();
		for (char c : nextLine.toCharArray()) {
			// if we found an opener just put it at the top of the stack
			if (openers.contains(c)) {
				stack.push(c);
			}
			else if (closers.contains(c)) {
				// the stack can't be empty when looking at a closer, otherwise
				// they don't match
				if (!stack.isEmpty()) {
					int closer_idx = closers.indexOf(c);// get the index of the
														// closer, it matches
														// the opener's index
					// if the top value in the stack doesn't match closer's
					// counterpart
					// return false can't be a match
					if (stack.peek() != openers.get(closer_idx)) {
						return false;
					} else {
						// otherwise we pop off the stack cause it was a match
						stack.pop();
					}

				} else {
					// if we have a closer but the stack is already empty
					return false;
				}
			}
		}
		return stack.isEmpty();
	}

	public static void main(String[] args) {
		// my weird way of doing test cases
		HashMap<String, Boolean> map = new HashMap<String, Boolean>();
		map.put("{{{{{{{{{adfkjaefia}}}}}}}", false);
		map.put("{{{{{{{{{[[[[[[kadfa{{{{{{{((({daljfdaf({{{[]}}kaldjfs})})))}}}}}}}]]]]]]}kjfela}}}}}}}}", true);
		map.put("{{{[}}}}dafda", false);
		map.put("{{{{{{{{{}}}}}}}}}", true);
		map.put("[[[[[[[[[kafjalfeianfailfeja;fjai;efa;sfj]]]]]]]]]kjajdain", true);
		map.put("", true);
		map.put("((((((fjdalfeja((((alefjalisj(())))))))))))d", true);
		map.put(")))(((d", false);
		map.put("({)}", false);
		for (String s : map.keySet()) {
			System.out.println("Expected output for:" + s + " is " + map.get(s));
			System.out.println("Actual output is: " + checkClosers(s) + "\n");
		}
	}
}
