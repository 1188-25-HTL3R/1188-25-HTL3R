package wordcount;

public enum State {
    WORD {
        @Override
        State handleChar(char c, WordCount counter) {
            if (!Character.isLetter(c)) {
                return NOWORD;
            }
            return WORD;
        }
    },
    NOWORD {
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
     * handles the next character in the text
     * @param c curr Character
     * @param counter current word count
     * @return the new state
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
}
