package enum1;


import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * Beschreibt einen Zustand im Text (beim Wörterzählen)
 */
public enum State {
    WORD,
    NOWORD;
}

class Main {
    /**
     * Zählt die Wörter in einem Text
     * @param s Text zu analysieren
     * @return Anzahl der Wörter
     */
    public static int count(String s) {
        State state = State.NOWORD;
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (state == State.NOWORD) {
                if (Character.isLetter(c)) {
                    state = State.WORD;
                    count++;
                }
            } else {
                if (!Character.isLetter(c)) state = State.NOWORD;
            }
        }
        return count;
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
