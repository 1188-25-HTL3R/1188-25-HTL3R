package csv;

import java.util.ArrayList;
import java.util.List;

public class CSVReader {
    enum State {
        READING {
            @Override
            void handle(char c, List<String> output, StringBuilder currString) {
                if (c == ',') {
                    output.add(currString.toString());
                    currString.setLength(0);
                } else {
                    currString.append(c);
                }
            }
        };

        /**
         * Schaut sich ein Zeichen an und entscheidet, was damit passieren soll.
         * @param c Das Zeichen, das betrachtet wird.
         * @param output Die Liste, in die die Teile des Strings geschrieben werden.
         * @param currString Der aktuell gelesene Teil des Strings.
         * @return Der neue Zustand.
         */
        abstract void handle(char c, List<String> output, StringBuilder currString);
    };

    public static String[] split(String line) {
        if (line.isEmpty()) return new String[0];
        List<String> output = new ArrayList<>();
        StringBuilder currString = new StringBuilder();
        State state = State.READING;
        for (char c : line.toCharArray()) {
            state.handle(c, output, currString);
        }
        output.add(currString.toString());
        return output.toArray(new String[0]);
    }
}
