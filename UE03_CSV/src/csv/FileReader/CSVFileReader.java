package csv;

import java.io.BufferedReader;
import java.io.Closeable;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.InvalidPathException;
import java.nio.file.Path;
import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * CSVFileReader reads a CSV file and manages its content
 */
public class CSVFileReader implements Closeable, Iterable<String[]> {
    /** Reads the File */
    private final BufferedReader reader;

    /** Reads and splits the CSV content */
    private final CSVReader csvReader;

    /**
     * Constructor
     * @param filename the name of the file to read
     * @throws InvalidPathException if the filename is invalid
     */
    public CSVFileReader(String filename) throws IOException {
        reader = Files.newBufferedReader(Path.of(filename));
        csvReader = new CSVReader();
    }


    /**
     * Changes the settings of the CSV reader
     * @param delimiter the delimiter character
     * @param quote the quote character
     * @param skipInitialWhitespace whether to skip initial whitespace
     */
    public void changeSettings(char delimiter, char quote, boolean skipInitialWhitespace) {
        csvReader.changeSettings(delimiter, quote, skipInitialWhitespace);
    }
    /**
     * Reads the next line of the CSV file
     * @return the next line of the CSV file
     * @throws IOException if an I/O error occurs
     */
    public String[] next() throws IOException {
        String nextLine = reader.readLine();
        if (nextLine == null) return null;
        return csvReader.split(nextLine);
    }

    @Override
    public void close() throws IOException {
        reader.close();
    }

@Override
public Iterator<String[]> iterator() {
    return new Iterator<String[]>() {
        private String[] nextLineBuffer;

        {
            // Initialize the buffer with the first line
            try {
                nextLineBuffer = CSVFileReader.this.next();
            } catch (IOException e) {
                throw new RuntimeException("Error reading the CSV file", e);
            }
        }

        @Override
        public boolean hasNext() {
            return nextLineBuffer != null;
        }

        @Override
        public String[] next() {
            if (nextLineBuffer == null) {
                throw new NoSuchElementException("No more lines in the CSV file");
            }
            String[] currentLine = nextLineBuffer;
            try {
                nextLineBuffer = CSVFileReader.this.next();
            } catch (IOException e) {
                throw new RuntimeException("Error reading the CSV file", e);
            }
            return currentLine;
        }
    };
}
}
