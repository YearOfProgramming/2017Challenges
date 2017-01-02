import java.util.Scanner;

public class ReverseString {

	public ReverseString() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
				Scanner user_input = new Scanner(System.in);
				String s = user_input.next();
				StringBuffer o = new StringBuffer(s.length());
				//why am I using StringBuffer instead of just adding strings together?
				//StringBuffer is more efficient at handling operations that involve handling values that aren't known at compile time.
				//Using: "aString" + "anotherString" to join strings is done at compile time if both strings are known, otherwise:
				//at run-time, the JVM creates a third string and copies both string's characters into this third one,
				//before deleting both of the previous strings, and reassiging the new string into their place. Expensive.
				for (int i = s.length()-1; i >= 0; i--){
					o.append(s.charAt(i));
				}
				System.out.println(o);
				user_input.close();
			}

}
