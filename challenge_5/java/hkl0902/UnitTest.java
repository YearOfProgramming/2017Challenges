import ucb.junit.textui;
import org.junit.Test;
import static org.junit.Assert.*;
import java.util.List;
import java.util.ArrayList;

public class UnitTest {
    public static void main (String [] ignored) {
        textui.runClasses(UnitTest.class);
    }

    List<Character> test = new ArrayList<Character>();
    List<Character> solution = new ArrayList<Character>();

    public void setUp() {
        test.add('x');
        test.add('k');
        test.add('w');
        test.add('b');
        test.add('l');
        test.add('p');
        test.add('q');
        test.add('a');
        test.add('v');
        test.add('e');
        test.add('t');
        test.add('i');
        solution.add('a');
        solution.add('b');
        solution.add('e');
        solution.add('i');
        solution.add('k');
        solution.add('l');
        solution.add('p');
        solution.add('q');
        solution.add('t');
        solution.add('v');
        solution.add('w');
        solution.add('x');
    }

    public void terminate() {
        test = new ArrayList<Character>();
        solution = new ArrayList<Character>();
    }

    @Test
    public void testQuickSort() {
        setUp();
        List<Character> sorted = FindTheDifference.quicksort(test);
        assertArrayEquals(solution.toArray(), sorted.toArray());
        terminate();
    }

    @Test
    public void findTheDifference() {
        String s = "xkwblpqaveti";
        String t = "kwxlbgpqevait";
        FindTheDifference ftd = new FindTheDifference(s, t);
        assertEquals('g', ftd.getTheDifference());
        // test edge case
        t = s + 'z';
        ftd = new FindTheDifference(s, t);
        assertEquals('z', ftd.getTheDifference());
    }

}
