__author__ = "Luka Pacar"
from typing import List, Set, Tuple

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
        :param laenge: Die Länge der Teilstrings
        :return: Ein Set mit den Abständen aller Wiederholungen der Teilstrings in text
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()