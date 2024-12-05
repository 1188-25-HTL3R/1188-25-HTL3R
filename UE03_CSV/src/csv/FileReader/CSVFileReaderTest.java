package csv.FileReader;
import csv.CSVFileReader;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static csv.matrix.Adjazenzmatrix.*;
import static org.junit.Assert.assertArrayEquals;

public class CSVFileReaderTest {
    @Test
    public void iterable_interfacee() {
        try {
            List<List<String>> expected =List.of(
                    List.of("1", "DD37Cf93aecA6Dc", "Sheryl", "Baxter", "Rasmussen Group", "East Leonard", "Chile", "229.077.5154", "397.884.0519x718", "zunigavanessa@smith.info", "2020-08-24", "http://www.stephenson.com/"),
                    List.of("2", "1Ef7b82A4CAAD10", "Preston", "Lozano", "Vega-Gentry", "East Jimmychester", "Djibouti", "5153435776", "686-620-1820x944", "vmata@colon.com", "2021-04-23", "http://www.hobbs.com/")
                    );

            CSVFileReader csvFileReader = new CSVFileReader("src/csv/FileReader/test.csv");
            List<List<String>> actual = new ArrayList<>();
            for (String[] strings : csvFileReader) {
                actual.add(Arrays.asList(strings));
            }
            assert actual.equals(expected);
        } catch (Exception ignored) {
            ignored.printStackTrace();
        }
    }
    @Test
    public void closable_interfacee() {
        try (CSVFileReader csvFileReader = new CSVFileReader("src/csv/FileReader/test.csv")) {
            // Dummy Test
            assert
            Arrays.stream(csvFileReader.next()).toList()
            .equals( List.of("1", "DD37Cf93aecA6Dc", "Sheryl", "Baxter", "Rasmussen Group", "East Leonard", "Chile", "229.077.5154", "397.884.0519x718", "zunigavanessa@smith.info", "2020-08-24", "http://www.stephenson.com/"));
        } catch (Exception ignored) {
            ignored.printStackTrace();
        }
    }

}
