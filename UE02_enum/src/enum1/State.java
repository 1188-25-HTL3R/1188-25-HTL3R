package enum1;


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
}
