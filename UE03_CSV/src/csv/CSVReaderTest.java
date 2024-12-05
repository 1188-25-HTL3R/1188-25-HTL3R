package csv;

import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertThrows;

public class CSVReaderTest {
    @Test
    public void simple_csv_test() {
        CSVReader csvReader = new CSVReader();
        assertArrayEquals(new String[] {"one", "two", "three"}, csvReader.split("one,two,three"));
        assertArrayEquals(new String[] {}, csvReader.split(""));
        assertArrayEquals(new String[] {"one"}, csvReader.split("one"));
        assertArrayEquals(new String[] {"one", "two", "three", ""}, csvReader.split("one,two,three,"));
        assertArrayEquals(new String[] {"one", "", "two", "", "", "three"}, csvReader.split("one,,two,,,three"));
    }

    @Test
    public void doublequote_csv_test() {
        CSVReader csvReader = new CSVReader();
        assertArrayEquals(new String[] {"uno", "dos", "tres, cuatro", "cinco"}, csvReader.split("\"uno\",dos,\"tres, cuatro\",cin\"co\""));
        assertThrows(IllegalArgumentException.class, () -> csvReader.split("\"nicht\"ok"));
        assertThrows(IllegalArgumentException.class, () -> csvReader.split("\"nicht ok"));
        assertArrayEquals(new String[] {"unodostresquoatr", "dos", "tres, cuatro", "cinco"}, csvReader.split("un\"od\"ost\"res\"quo\"atr\",dos,\"tres, cuatro\",ci\"nco\""));
    }

    @Test
    public void whitespaces_csv_test() {
        CSVReader csvReader = new CSVReader();
        assertArrayEquals(new String[] {"uno", "dos", "tres, cuatro", "cinco"}, csvReader.split("  \"uno\",  dos,   \"tres, cuatro\",  cin\"co\""));
        assertThrows(IllegalArgumentException.class, () -> csvReader.split("  \"nicht\"ok"));
        assertThrows(IllegalArgumentException.class, () -> csvReader.split("  \"nicht ok"));
        assertArrayEquals(new String[] {"unodostresquoatr", "dos", "tres, cuatro", "cinco"}, csvReader.split("     un\"od\"ost\"res\"quo\"atr\",dos,\"tres, cuatro\",ci\"nco\""));
    }

    @Test
    public void skip_inital_space_csv_test() {
        CSVReader csvReader = new CSVReader();
        assertArrayEquals(new String[] {"uno", "dos", "tres, cuatro", "cinco"}, csvReader.split("  \"uno\",  dos,   \"tres, cu\"\"atro\",  cin\"co\""));
        assertThrows(IllegalArgumentException.class, () -> csvReader.split("  \"nicht\"ok"));
        assertThrows(IllegalArgumentException.class, () -> csvReader.split("  \"nicht ok"));
        assertArrayEquals(new String[] {"unodostresquoatr", "dos", "tres, cuatro", "cinco"}, csvReader.split("     un\"od\"ost\"re\"\"s\"quo\"atr\",dos,\"tre\"\"s, cuatro\",ci\"n\"\"co\""));
    }
     @Test
    public void constructor_csv_test() {
        CSVReader csvReader = new CSVReader('-','\'',false);
        assertArrayEquals(new String[] {"  uno", "  dos", "   tres, cuatro", "  cinco"}, csvReader.split("  'uno'-  dos-   'tres, cu''atro'-  cin'co'"));
        assertThrows(IllegalArgumentException.class, () -> csvReader.split("  'nicht'ok"));
        assertThrows(IllegalArgumentException.class, () -> csvReader.split("  'nicht ok"));
        assertArrayEquals(new String[] {"     unodostresquoatr", "dos", "tres- cuatro", "cinco"}, csvReader.split("     un'od'ost're''s'quo'atr'-dos-'tre''s- cuatro'-ci'n''co'"));
    }
}
