import java.util.*;
import java.io.IOException;

public class StringReverserImpl implements StringReverser {

    public String reverse(String stringToReverse) throws IOException {
        checkInput(stringToReverse);
        return new StringBuilder(stringToReverse).reverse().toString();
    }

    // Ideally this job is done but special 3rd party lib, like Apache Commons / Google Guava
    private void checkInput(String stringToReverse) throws IOException {
        if(stringToReverse == null) throw new IOException("Your string is null");
        if(stringToReverse.length() == 0) throw new IOException("Empty string is a bad input");
    }

}
