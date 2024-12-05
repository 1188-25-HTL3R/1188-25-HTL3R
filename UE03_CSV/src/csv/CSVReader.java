package csv;

import java.util.ArrayList;
import java.util.List;

public class CSVReader {
    private enum State {
        READING {
            @Override
            State handle(char c, StringBuilder currString, CSVReader csvReader) {
                return handleBasic(c, currString, READING, csvReader);
            }

            @Override
            List<String> handleEnd(StringBuilder currString, CSVReader csvReader) {
                if (!currString.isEmpty()) addToOutput(currString, csvReader);
                return getOutput(csvReader);
            }
        },
        READING_AFTER_DOUBLE_QUOTE {
            @Override
            State handle(char c, StringBuilder currString, CSVReader csvReader) {
                if (c == csvReader.DELIMITER_CHAR) throw new IllegalArgumentException("Invalid CSV format - There can not be text after a double quote");
                return handleBasic(c, currString, READING_AFTER_DOUBLE_QUOTE, csvReader);
            }

            @Override
            List<String> handleEnd(StringBuilder currString, CSVReader csvReader) {
                throw new IllegalArgumentException("Invalid CSV format - There can not be text after a double quote");
            }
        },
        AFTER_DOUBLE_QUOTE {
            @Override
            State handle(char c, StringBuilder currString, CSVReader csvReader) {
                return handleBasic(c, currString, READING_AFTER_DOUBLE_QUOTE, csvReader);
            }

            @Override
            List<String> handleEnd(StringBuilder currString, CSVReader csvReader) {
                addToOutput(currString, csvReader);
                return getOutput(csvReader);
            }
        },
        DELIMITER {
            @Override
            State handle(char c, StringBuilder currString, CSVReader csvReader) {
                addToOutput(currString, csvReader);
                if (csvReader.SKIP_INITIAL_WHITESPACE && Character.isWhitespace(c)) return IN_WHITESPACE;
                return State.handleBasic(c, currString, READING, csvReader);
            }

            @Override
            List<String> handleEnd(StringBuilder currString, CSVReader csvReader) {
                addToOutput(currString, csvReader);
                addToOutput(new StringBuilder(), csvReader);
                return getOutput(csvReader);
            }
        },
        IN_WHITESPACE {
            @Override
            State handle(char c, StringBuilder currString, CSVReader csvReader) {
                if (Character.isWhitespace(c)) return this;
                return handleBasic(c, currString, READING, csvReader);
            }

            @Override
            List<String> handleEnd(StringBuilder currString, CSVReader csvReader) {
                State.addToOutput(currString, csvReader);
                return getOutput(csvReader);
            }
        },
        FIRST_DOUBLE_QUOTE {
            @Override
            State handle(char c, StringBuilder currString, CSVReader csvReader) {
                currString.append(c);
                if (c == csvReader.DOUBLE_QUOTE_CHAR) {
                    return READING;
                }
                return IN_DOUBLE_QUOTE;
            }

            @Override
            List<String> handleEnd(StringBuilder currString, CSVReader csvReader) {
                throw new IllegalArgumentException("Invalid CSV format - Cannot end in a double quote");
            }
        },
        IN_DOUBLE_QUOTE {
            @Override
            State handle(char c, StringBuilder currString, CSVReader csvReader) {
                if (c == csvReader.DOUBLE_QUOTE_CHAR) return AFTER_DOUBLE_QUOTE;
                currString.append(c);
                return IN_DOUBLE_QUOTE;
            }

            @Override
            List<String> handleEnd(StringBuilder currString, CSVReader csvReader) {
                throw new IllegalArgumentException("Invalid CSV format - Cannot end in a double quote");
            }
        };



        /**
         * Handles the given character in a basic way. <br>
         * A lot of States use the same basic handling, so this method is used to avoid code duplication.
         * @param c character to handle
         * @param currString current string
         * @return next state
         */
        private static State handleBasic(char c, StringBuilder currString, State defaultState, CSVReader csvReader) {
            if (c == csvReader.DELIMITER_CHAR) return DELIMITER;
            if (c == csvReader.DOUBLE_QUOTE_CHAR) return FIRST_DOUBLE_QUOTE;
            currString.append(c);
            return defaultState;
        }

        /**
         * Adds the current string to the output and resets it
         * @param currString current string
         */
        private static void addToOutput(StringBuilder currString, CSVReader csvReader) {
            csvReader.output.add(currString.toString());
            currString.setLength(0);
        }

        /**
         * Handles the given character
         * @param c character to handle
         * @param currString
         */
        abstract State handle(char c, StringBuilder currString, CSVReader csvReader);

        /**
         * Handles the end of the line
         * @param currString current string
         */
        abstract List<String> handleEnd(StringBuilder currString, CSVReader csvReader);

        /** Returns the Output List */
        private static List<String> getOutput(CSVReader csvReader) {
            List<String> outputCopy = new ArrayList<>(csvReader.output);
            csvReader.output.clear();
            return outputCopy;
        }
    };

    /** Character used to delimit */
    private char DELIMITER_CHAR = ',';
    /** Character used to quote */
    private char DOUBLE_QUOTE_CHAR = '"';
    /** Flag to skip initial whitespace */
    private boolean SKIP_INITIAL_WHITESPACE = true;
    /** Output list */
    private List<String> output = new ArrayList<>();


    /**
     * Changes the settings of the CSVReader
     * @param delimiter character used to delimit
     * @param doublequote character used to quote
     * @param skipInitialWhitespace flag to skip initial whitespace
     */
    public void changeSettings(char delimiter, char doublequote, boolean skipInitialWhitespace) {
        DELIMITER_CHAR = delimiter;
        DOUBLE_QUOTE_CHAR = doublequote;
        SKIP_INITIAL_WHITESPACE = skipInitialWhitespace;
    }

    /**
     * Constructor for CSVReader
     * @param delimiter character used to delimit
     * @param doublequote character used to quote
     * @param skipInitialWhitespace flag to skip initial whitespace
     */
    public CSVReader(char delimiter, char doublequote, boolean skipInitialWhitespace) {
        changeSettings(delimiter, doublequote, skipInitialWhitespace);
    }
    /**
     * Constructor for CSVReader. <br>
     * Initiates the Reader with following parameters:
     * <ul>
     *     <li>Delimiter: ','</li>
     *     <li>Doublequote: '"'</li>
     *     <li>Skip Initial Whitespace: true</li>
     * </ul>
     *
     */
    public CSVReader() {}
    /**
     * Splits the given csv-line into an array of strings
     * @param line line to split
     * @return array of strings
     */
    public String[] split(String line) {
        if (line.isEmpty()) return new String[0];

        StringBuilder currString = new StringBuilder();
        State state = SKIP_INITIAL_WHITESPACE ? State.IN_WHITESPACE : State.READING;
        for (char c : line.toCharArray()) {
            state = state.handle(c, currString, this);
        }

        return state.handleEnd(currString, this).toArray(new String[0]);
    }
}
