import java.util.Scanner; // Import Scanner for user Input
public class Application {
  public static void main(String[] args) {
    System.out.println("Enter a string to be reversed");
    Scanner sb = new Scanner(System.in);
    String s = sb.nextLine();
    System.out.println(new StringBuilder(s).reverse());
  }
}
