package wordcount;
import org.junit.Test;

import static enum1.Main.count;
import static org.junit.Assert.assertEquals;
import static wordcount.WordCount.*;
public class StateTest {
    @Test
    public void test() {
        // Tests für simple Wordcount
        assertEquals(2, count("Hello world!"));
        assertEquals(3, count("Hello    world  again!"));
        assertEquals(0, count(""));
        assertEquals(0, count("    "));
        assertEquals(1, count("Hello"));
        assertEquals(2, count("HALLO??"));
        assertEquals(3, count("TTT???HAL??LO??"));
        assertEquals(4, count("Hallöchen, wie geht es dir?"));
        assertEquals(5, count("Hallo, ich das ist ein Test"));
        assertEquals(0, count("!@#$%^&*()"));
        assertEquals(0, count("1234 5678"));
        assertEquals(3, count("Java 8 is cool"));
        assertEquals(4, count("Ich bin der Luka"));
        assertEquals(7, count("This is    a test of multiple   lines"));
        assertEquals(0, count(""));
    }
}
