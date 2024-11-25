package csv;

import org.junit.Test;

import java.util.Arrays;

import static csv.CSVReader.*;
import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

public class CSVReaderTest {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(split("one,two,three")));
    }
    @Test
    public void simple_csv_test() {
        assertArrayEquals(new String[] {"one", "two", "three"}, split("one,two,three"));
        assertArrayEquals(new String[] {}, split(""));
        assertArrayEquals(new String[] {"one"}, split("one"));
        assertArrayEquals(new String[] {"one", "two", "three", ""}, split("one,two,three,"));
        assertArrayEquals(new String[] {"one", "", "two", "", "", "three"}, split("one,,two,,,three"));
    }
}
