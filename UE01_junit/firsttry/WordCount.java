package firsttry;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/*
 * author: Luka Pacar 4CN
 * date: 14.10.2024
 */
public class WordCount {

    public static Pattern wordCountPattern = Pattern.compile("(?<=^|\\W)+\\w+(?=\\W+|$)");

    public static int count(String input) {
        Matcher m = wordCountPattern.matcher(removeHTMLBrackets(input));
        int wordCount = 0;
        while (m.find()) wordCount++;
        return wordCount;
    }

    private static String removeHTMLBrackets(String input) {
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c == '<') { // Findet eine öffnende Klammer
                int klammerCount = 1;
                int lastClosedKlammer = -1;
                for (int j = i + 1; j < input.length(); j++) {
                    char c2 = input.charAt(j);
                    /*
                     * Zählt die Depth der Klammern. Z.B. <<>> hat eine max. Depth von 2.
                     * Dabei merke ich mir die letzte schließende Klammer.
                     * Ich suche nach einer schließenden Klammer, die auf der gleichen Depth ist wie die öffnende Klammer.
                     * -> Wenn ich eine schließende Klammer finde, die auf der gleichen Depth ist, dann entferne ich den Inhalt der Klammern.
                     * -> Wenn ich das ende Erreiche, dann suche ich die letzte schließende Klammer und entferne den Inhalt bist dort (gibt es keine schließende Klammer, dann wird alles bis zum Ende entfernt)
                     * Bei einer ungeraden Anzahl von Anführungszeichen in der Klammer werden alle Wörter danach nicht gezählt.
                     */
                    if (c2 == '<') klammerCount++;
                    else if (c2 == '>' || j == input.length() - 1) {
                        if (j == input.length() -1) {
                            String inbetween = input.substring(i, lastClosedKlammer == -1 ? input.length() : lastClosedKlammer + 1);
                            if (countAnfuehrungszeichen(inbetween) % 2 != 0) return input.substring(0,i);
                            return removeHTMLBrackets(  input.substring(0,i) + " " + (lastClosedKlammer == -1 ? "" : input.substring(lastClosedKlammer+1)));
                        }
                        lastClosedKlammer = j;
                        klammerCount--;
                        if (klammerCount == 0) {
                            for (int k = j + 1; k < input.length(); k++) {
                                if (input.charAt(k) == '>') j = k;
                                else if (input.charAt(k) == '<') break;
                            }
                            String inbetween = input.substring(i, j + 1);
                            if (countAnfuehrungszeichen(inbetween) % 2 != 0) return input.substring(0,i);
                            return removeHTMLBrackets(input.substring(0,i) + " " +  input.substring(j+1));
                        }
                    }
                }
            }
        }
        return input;
    }

    private static final Pattern findAnführungszeichen = Pattern.compile("(?<!\\\\)\"");
    private static int countAnfuehrungszeichen(String input) {
        Matcher m = findAnführungszeichen.matcher(input);
        int count = 0;
        while (m.find()) count++;
        return count;
    }
}
