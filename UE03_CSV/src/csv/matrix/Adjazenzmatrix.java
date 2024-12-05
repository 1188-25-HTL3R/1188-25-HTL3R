package csv.matrix;

import csv.CSVFileReader;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * Adjazenzmatrix reads a CSV file and manages its content
 */
public class Adjazenzmatrix {

    /**
     * Reads the Adjazenzmatrix from a CSV file
     * @param filename the name of the file to read
     * @return the Adjazenzmatrix
     */
    public static HashMap<String, List<String>> getAdjazenzmatrix(String filename) {
        try (csv.CSVFileReader csvFileReader = new CSVFileReader(filename)) {
            csvFileReader.changeSettings(';','"',true); // Delimiter auf ; ändern
            HashMap<String, List<String>> adjazenzmatrix = new HashMap<>();

            String[] headline = csvFileReader.next();
            for (String[] strings : csvFileReader) {
                List<String> list = new ArrayList<>();
                for (int i = 1; i < strings.length; i++) {
                    list.add(headline[i-1] +
                            ":" + (strings[i].isEmpty() ? "0" : strings[i]));
                }
                adjazenzmatrix.put(strings[0], list);
            }
            return adjazenzmatrix;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    /**
     * Prints the Adjazenzmatrix
     * @param adjazenzmatrix the Adjazenzmatrix
     * @return the Adjazenzmatrix as a String array
     */
    public static String[] printAdjazenzmatrix(HashMap<String, List<String>> adjazenzmatrix) {
        List<String> output = new ArrayList<>();
        for (String key : adjazenzmatrix.keySet()) {
            String line = key + ": ";
            List<String> inputList = adjazenzmatrix.get(key);
            for (int i = 0; i < inputList.size(); i++) {
                if (inputList.get(i).contains("0")) continue;
                line += "nach " + inputList.get(i) + ", ";
            }
            output.add(line.substring(0, line.lastIndexOf(",")));
        }
        return output.toArray(new String[0]);
    }
}
