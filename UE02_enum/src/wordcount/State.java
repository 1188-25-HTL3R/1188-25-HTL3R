package wordcount;
/* author: Luka Pacar 4CN */

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * Beschreibt einen Zustand im Text (beim Wörterzählen)
 */
public enum State {
    WORD { // Im Wort
        @Override
        State handleChar(char c, WordCount counter) {
            if (!Character.isLetter(c)) {
                return NOWORD;
            }
            return WORD;
        }
    },
    NOWORD { // Nicht im Wort
        @Override
        State handleChar(char c, WordCount counter) {
            if (Character.isLetter(c)) {
                counter.counter++;
                return WORD;
            }
            return NOWORD;
        }
    };

    /**
     * Behandelt den nächsten Character im Text
     * @param c curr Character
     * @param counter WordCount - Für Zählung
     * @return nächster Zustand
     */
    abstract State handleChar(char c, WordCount counter);
}
class WordCount {

    int counter = 0;

    public static int count(String s) {
        return new WordCount().countWords(s);
    }
    /**
     * Zählt die Wörter in einem Text
     * @param s Text zu analysieren
     * @return Anzahl der Wörter
     */
    public int countWords(String s) {
        counter = 0;
        State state = State.NOWORD;
        for (char c : s.toCharArray()) state = state.handleChar(c, this);
        return counter;
    }

    /**
     * Zählt die Wörter in einer Datei
     * @param file Datei zu analysieren
     * @return Anzahl der Wörter
     * @throws IOException Fehler beim Lesen der Datei
     */
    public static int count(Path file) throws IOException {
        int totalCount = 0;
        try (BufferedReader reader = Files.newBufferedReader(file)) {
            String line = "";
            while ((line=reader.readLine()) != null) {
                totalCount += count(line);
            }
        }
        return totalCount;
    }
}
