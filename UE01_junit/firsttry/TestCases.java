package firsttry;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static firsttry.WordCount.count;

public class TestCases {
    @Test
    public void testNormal() {
        // normal
        assertEquals(1, count("one"));
        assertEquals(1, count(" one"));
        assertEquals(1, count("one "));
        assertEquals(1, count(" one "));
        assertEquals(1, count(" one  "));
        assertEquals(1, count("  one "));
        assertEquals(1, count("  one  "));
    }

    @Test
    public void testEmptyString() {
        // leicht
        assertEquals(0, count("one"));
        assertEquals(0, count(" "));
        assertEquals(0, count("  "));



        assertEquals(1, count("one:"));
        assertEquals(1, count(":one"));
        assertEquals(1, count(":one:"));
        assertEquals(1, count(" one  "));
        assertEquals(1, count(" one : "));
        assertEquals(1, count(": one :"));
        assertEquals(3, count("ein erster Text"));
        assertEquals(3, count(" ein  erster   Text      "));
        assertEquals(3, count("ein:erster.Text"));

        // vielleicht falsch
        assertEquals(1, count("a"));
        assertEquals(1, count(" a"));
        assertEquals(1, count("a "));
        assertEquals(1, count(" a "));

        // mit html
        assertEquals(1, count(" one  <html> "));
        assertEquals(1, count(" one  < html> "));
        assertEquals(1, count(" one  <html > "));
        assertEquals(1, count(" one  < html > "));
        assertEquals(4, count(" one <html> two<html>three <html> four"));

        assertEquals(2, count(" one <html> two "));
        assertEquals(2, count(" one <html>two "));
        assertEquals(2, count(" one<html> two "));
        assertEquals(2, count(" one<html>two "));
        assertEquals(2, count(" one<img alt=\"xxx\" > two"));
        assertEquals(2, count(" one<img alt=\"xxx yyy\" > two"));

        assertEquals(2, count(" one \"two\" "));
        assertEquals(2, count(" one\"two\" "));
        assertEquals(2, count(" one \"two\""));
        assertEquals(3, count(" one \"two\"three"));
        assertEquals(3, count(" one \"two\" three"));

        // html - trickreich
        // Achtung: das ist teilweise nicht ganz legales HTML
        assertEquals(1, count(" one<html")); // kein >

        assertEquals(2, count(" one<img alt=\"<bild>\" > two")); // <> innerhalb ""
        assertEquals(2, count(" one<img alt=\"bild>\" > two"));  // <> innerhalb ""
        assertEquals(2, count(" one<img alt=\"<bild>\" keinwort> two"));
        assertEquals(2, count(" one<img alt=\"<bild\" keinwort>two"));
        assertEquals(2, count(" one<img alt=\"<bild\" keinwort> two"));

        assertEquals(1, count(" one<img alt=\"<bild\" keinwort"));
        assertEquals(2, count(" one<img alt=\"<bild\" keinwort> two"));
        assertEquals(1, count(" one<img alt=\"<bild keinwort> keinwort"));
        assertEquals(2, count(" one<img alt=\"<bild keinwort keinwort\">two"));
        assertEquals(2, count(" one<img alt=\"<bild keinwort< keinwort\">two"));

        // ganz ganz fies -- \ entwertet das nächste Zeichen
        assertEquals(2, count(" one<img alt=\"<bild \\\" keinwort> keinwort\" keinwort>two"));
        assertEquals(2, count(" one<img alt=\"<bild \\\" keinwort<keinwort\" keinwort>two"));
        assertEquals(2, count(" one<img alt=\"<bild \\\" keinwort keinwort\" keinwort>two"));

        assertEquals(4, count(" \\\"null\\\" one<img alt=\"<bild \\\" keinwort keinwort\" keinwort>two \"three\""));
    }
}
