__author__ = "Luka Pacar"
from typing import List, Set, Tuple
from collections import Counter


class Kasiski:
    """
    Der Kasiski-Test ist ein Verfahren zur Entschlüsselung von Texten, die mit der Vigenère-Chiffre verschlüsselt
    wurden. Wir implementieren die Klasse Kasiski, die dabei hilft, die Vigenère-Chiffre zu knacken
    """

    def __init__(self, crypt_text:str=""):
        self.crypt_text = crypt_text

    def allpos(self, text:str, teilstring:str) -> List[int]:
        """
        Gibt eine Liste zurück, die die Positionen von teilstring in text angibt.

        :type text: str
        :param text: der Text, in dem gesucht wird
        :type teilstring: str
        :param teilstring: der zu suchende Teilstring
        :return: die Positionen von teilstring in text
        :rtype: List[int]

        Berechnet die Positionen von teilstring in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]
        >>> k.allpos("heissajuchei, ein ei", "hai")
        []
        """
        length = len(teilstring)
        positions = [] # Positionen der Substrings

        for i in range(len(text)-length+1):
            if text[i:i+length] == teilstring:
                positions.append(i)

        return positions

    def alldist(self, text:str, teilstring:str) -> Set[int]:
        """
        Berechnet die Abstände zwischen allen Vorkommnissen des Teilstrings im verschlüsselten Text.

        :param text: Der verschlüsselte Text
        :param teilstring: Der zu suchende Teilstring
        :return: Ein Set mit den Abständen aller Wiederholungen des Teilstrings in text
        :rtype: Set[int]
        :type text: str
        :type teilstring: str

        >>> k = Kasiski()
        >>> k.alldist("heissajuchei, ein ei", "ei")
        {4, 8, 9, 13, 17}
        >>> k.alldist("heissajuchei, ein ei", "hai")
        set()
        """
        get_pos = self.allpos(text, teilstring)
        dist = set()
        for first_pointer in range(len(get_pos)):
            for second_pointer in range(first_pointer+1,len(get_pos)):
                dist.add(get_pos[second_pointer] - get_pos[first_pointer])
        return dist

    def dist_n_tuple(self, text:str, laenge:int) -> Set[Tuple[str, int]]:
        """
        Überprüft alle Teilstrings aus text mit der gegebenen laenge und liefert ein Set
        mit den Abständen aller Wiederholungen der Teilstrings in text.

        :param text: Der verschlüsselte Text
        :param laenge: die Länge der Teilstrings
        :return: ein Set mit den Abständen aller Wiederholungen der Teilstrings in text
        :rtype: Set[Tuple[str, int]]
        :type text: str
        :type laenge: int


        >>> k = Kasiski()
        >>> k.dist_n_tuple("heissajuchei", 2) == {('ei', 9), ('he', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 3) == {('hei', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 4) == set()
        True
        >>> k.dist_n_tuple("heissajucheieinei", 2) == \
        {('ei', 5), ('ei', 14), ('ei', 3), ('ei', 9), ('ei', 11), ('he', 9), ('ei', 2)}
        True
        """
        dist = set()
        for i in range(len(text) - laenge):
            string = text[i:i+laenge]
            for distance in self.alldist(text, string):
                dist.add((string, distance))

        return dist

    def dist_n_list(self, text:str, laenge:int) -> List[int]:
        """
        Wie dist_tuple, liefert aber nur eine aufsteigend sortierte Liste der
        Abstände ohne den Text zurück. In der Liste soll kein Element mehrfach vorkommen.

        :param text: Der verschlüsselte Text
        :param laenge: die Länge der Teilstrings
        :return: eine Liste mit den Abständen aller Wiederholungen der Teilstrings in text
        :rtype: List[int]
        :type text: str
        :type laenge: int

        >>> k = Kasiski()
        >>> k.dist_n_list("heissajucheieinei", 2)
        [2, 3, 5, 9, 11, 14]
        >>> k.dist_n_list("heissajucheieinei", 3)
        [9]
        >>> k.dist_n_list("heissajucheieinei", 4)
        []
        """
        dist = set()
        for _, distance in self.dist_n_tuple(text, laenge):
                dist.add(distance)
        return sorted(list(dist))

    def ggt(self, x:int, y:int)->int:
        """
        Ermittelt den größten gemeinsamen Teiler von x und y.

        :param x: der erste Wert
        :param y: der zweite Wert

        >>> k = Kasiski()
        >>> k.ggt(10, 25)
        5
        >>> k.ggt(10, 25)
        5
        """
        if min(x, y) == 0:
            return max(x, y)
        else:
            return self.ggt(min(x, y), max(x,y)%min(x,y))

    def ggt_count(self, zahlen:List[int])->Counter:
        """
        Bestimmt die Häufigkeit der paarweisen ggt aller Zahlen aus list.

        :param zahlen: Eine Liste von Zahlen
        :type zahlen: List[int]
        :return: Ein Counter-Objekt, das die Häufigkeit der paarweisen ggt aller Zahlen aus list enthält.
        :rtype: Counter

        >>> k = Kasiski()
        >>> k.ggt_count([12, 14, 16])
        Counter({2: 2, 12: 1, 4: 1, 14: 1, 16: 1})
        >>> k.ggt_count([10, 25, 50, 100])
        Counter({10: 3, 25: 3, 50: 2, 5: 1, 100: 1})
        """
        occ = []
        for i in range(len(zahlen)):
            for j in range(i, len(zahlen)):
                occ.append(self.ggt(zahlen[i], zahlen[j]))
        return Counter(occ)

    def get_nth_letter(self, s:str, start:int, n:int)->str:
        """
        Extrahiert aus s jeden n. Buchstaben beginnend mit index start.
        Usage examples:
        >>> k = Kasiski()
        >>> k.get_nth_letter("Das ist kein kreativer Text.", 1, 4)
        'asektrx'
        """
        output = ""
        i = start
        while i < len(s):
            output += s[i]
            i += n
        return output

    def crack_key(len:int)->str:
        """
        Knackt den Schlüssel der Vigenère-Chiffre mit der gegebenen Schlüssellänge.

        :param len: Die Länge des Schlüssels
        :type len: int
        :return: der Schlüssel
        :rtype: str
        """

        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()