package secondtry;
/* author: Luka Pacar 4CN */

/**
 * Beschreibt den Zustand aktuell im Text
 */
public enum State {
    WORD { // Im Wort
        @Override
        public State handleChar(char c, MainWordCount counter) {
            if (c == '<') return IN_BRACKET;
            if (Character.isLetter(c)) return WORD;
            return NOWORD;
        }
    },
    NOWORD { // Nicht im Wort
        @Override
        public State handleChar(char c, MainWordCount counter) {
            if (c == '<') return IN_BRACKET;
            if (Character.isLetter(c)) {
                counter.counter++;
                return WORD;
            }
            return NOWORD;
        }
    },
    IN_BRACKET { // In einer Klammer
        @Override
        public State handleChar(char c, MainWordCount counter) {
            if (c == '\\') return IN_BRACKET_ESCAPED;
            if (c == '"') return IN_QUOTE;
            if (c == '>') return NOWORD;
            return IN_BRACKET;
        }
    },
    IN_BRACKET_ESCAPED { // In einer Klammer mit Escapesequenz
        @Override
        public State handleChar(char c, MainWordCount counter) {
            return IN_BRACKET;
        }
    },
    IN_QUOTE_ESCAPED { // In Anführungszeichen mit Escapesequenz
        @Override
        public State handleChar(char c, MainWordCount counter) {
            return IN_QUOTE;
        }
    },
    IN_QUOTE { // In Anführungszeichen
        @Override
        public State handleChar(char c, MainWordCount counter) {
            if (c == '\\') return IN_QUOTE_ESCAPED;
            if (c == '"') return IN_BRACKET;
            return IN_QUOTE;
        }
    };

    /**
     * handles the next character in the text
     * @param c curr Character
     * @param counter current word count
     * @return the new state
     */
    public abstract State handleChar(char c, MainWordCount counter);
}
class MainWordCount {

    /** Counts the words in a text */
    int counter = 0;

    /**
     * Zählt die Wörter in einem Text
     * @param s Text zu analysieren
     * @return Anzahl der Wörter
     */
    public int countWords(String s) {
        counter = 0;
        State currState = State.NOWORD;
        for (char c : s.toCharArray()) currState = currState.handleChar(c, this);
        return counter;
    }

    /**
     * Zählt die Wörter in einem Text
     * @param s Text zu analysieren
     * @return Anzahl der Wörter
     */
    public static int count(String s) {
        return new MainWordCount().countWords(s);
    }
}
