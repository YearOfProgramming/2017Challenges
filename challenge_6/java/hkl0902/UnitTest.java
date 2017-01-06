import ucb.junit.textui;
import org.junit.Test;
import static org.junit.Assert.*;
import java.util.List;
import java.util.ArrayList;

public class UnitTest {
    public static void main (String [] ignored) {
        textui.runClasses(UnitTest.class);
    }

    @Test
    public void testRangeToString() {
        RangeList<Integer> rl = new RangeList<Integer>();

        rl.add(1);
        rl.add(2);
        rl.add(3);
        rl.add(4);

        assertEquals("1->4", rl.toString());

        rl.clear();

        assertEquals(null, rl.toString());

        rl.add(1);
        assertEquals(null, rl.toString());
        rl.add(2);
        assertEquals("1->2", rl.toString());

        rl.clear();
        rl.add(5);
        rl.add(6);
        rl.add(7);
        rl.add(8);
        rl.add(9);
        rl.add(10);
        assertEquals("5->10", rl.toString());
    }

    @Test
    public void testChallenge() {
        Ranges r = new Ranges(new int[] {1, 2, 3, 4, 5, 6});
        assertArrayEquals(new String[] {"1->6"}, r.rangesString());
        r = new Ranges(new int[] {1,2,3,4,8,9,10,12,13,14});
        assertArrayEquals(new String[] {"1->4", "8->10", "12->14"}, r.rangesString());
        r = new Ranges(new int[] {1,2,3,4,8,9,10,12,13,14,20,21,22,23});
        assertArrayEquals(new String[] {"1->4", "8->10", "12->14", "20->23"}, r.rangesString());
        r = new Ranges(new int[] {1});
        assertArrayEquals(new String[] {}, r.rangesString());
        r = new Ranges(new int[] {});
        assertArrayEquals(new String[] {}, r.rangesString());
    }



}
