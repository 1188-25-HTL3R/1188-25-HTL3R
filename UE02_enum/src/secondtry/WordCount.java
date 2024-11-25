package secondtry;
import org.junit.Test;

import java.nio.file.Path;

import static org.junit.Assert.assertEquals;
import static org.testng.AssertJUnit.assertEquals;
import static secondtry.MainWordCount.count;

public class WordCount {
    @Test
    public void easy() {
        assertEquals(0,count(""));
        assertEquals(0,count(" "));
        assertEquals(0,count("  "));
        assertEquals(1, count("a"));
        assertEquals(1, count(" a"));
        assertEquals(1, count("a "));
        assertEquals(1, count(" a "));
    }
    @Test
    public void normal() {
        assertEquals(1, count("one"));
        assertEquals(1, count(" one"));
        assertEquals(1, count("one "));
        assertEquals(1, count(" one "));
        assertEquals(1, count(" one  "));
        assertEquals(1, count("  one "));
        assertEquals(1, count("  one  "));
    }
    @Test
    public void hard() {
        assertEquals(1, count("one:"));
        assertEquals(1, count(":one"));
        assertEquals(1, count(":one:"));
        assertEquals(1, count(" one  "));
        assertEquals(1, count(" one : "));
        assertEquals(1, count(": one :"));
        assertEquals(3, count("ein erster Text"));
        assertEquals(3, count(" ein  erster   Text      "));
        assertEquals(3, count("ein:erster.Text"));

    }
    @Test
    public void html_easy() {
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
    }
    @Test
    public void html_normal() {
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
    }
    @Test
    public void html_hard() {
        assertEquals(2, count(" one<img alt=\"<bild \\\" keinwort> keinwort\" keinwort>two"));
        assertEquals(2, count(" one<img alt=\"<bild \\\" keinwort<keinwort\" keinwort>two"));
        assertEquals(2, count(" one<img alt=\"<bild \\\" keinwort keinwort\" keinwort>two"));
        assertEquals(4, count(" \\\"null\\\" one<img alt=\"<bild \\\" keinwort keinwort\" keinwort>two \"three\""));
    }
    @Test
    public void html_file() {
        try {
            // Vom Code der letzten Übung 470528
            assertEquals(470528,count(Path.of("src/crsto12.html")));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
