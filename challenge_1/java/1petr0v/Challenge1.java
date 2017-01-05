import java.io.IOException;

public class Challenge1 {

    public static void main(String ... args) {
        if(args.length != 1) {
            System.err.println("Illegal number of arguments");
            System.exit(-1);
        }

        StringReverser reverser = new StringReverserImpl();
        try {
            System.out.println(reverser.reverse(args[0]));
        } catch(IOException e) {
            System.err.println("Could not reverse string. Please check your input.");
        }
    }

}
