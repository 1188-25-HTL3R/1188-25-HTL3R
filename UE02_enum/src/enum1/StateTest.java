package enum1;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static enum1.Main.*;

public class StateTest {
    @Test
    public void simple_wordcount() {
        // Tests für simple Wordcount
        assertEquals(2, count("Hello world!"));
        assertEquals(3, count("Hello    world  again!"));
        assertEquals(0, count(""));
        assertEquals(0, count("     "));
        assertEquals(1, count("Hello"));
        assertEquals(2, count("Hello, world!"));
        assertEquals(3, count("Hello\nworld\nagain!"));
        assertEquals(6, count("Hello\tworld   this is\ta test."));
        assertEquals(1, count("Wow!"));
        assertEquals(0, count("!@#$%^&*()"));
        assertEquals(0, count("1234 5678"));
        assertEquals(3, count("Java 8 is cool"));
        assertEquals(5, count("This is a known fact"));
        assertEquals(7, count("This is    a test of multiple  spaces"));
        assertEquals(0, count(""));
    }
}
