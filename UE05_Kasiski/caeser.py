__author__ = "Luka Pacar"
from collections import Counter
from typing import List, Tuple
import string


class Caesar:
    """
    Die Klasse Caesar verschlüsselt und entschlüsselt Texte mit dem Caesar-Verfahren.
    Der Caesar-Algorithmus ist ein symmetrisches Verschlüsselungsverfahren, bei dem jeder Buchstabe
    des Klartextes um einen konstanten Wert verschoben wird. Der Wert wird als Schlüssel bezeichnet.
    Der Schlüssel ist ein Buchstabe, der definiert, um wie viele Zeichen verschoben wird.
    """

    def __init__(self, encryption_key:str = None):
        """
        Initialisiert die Klasse Caesar mit einem optionalem Verschlüsselungsschlüssel.
        :param encryption_key: Der Verschlüsselungsschlüssel
        :type encryption_key: str

        :raises ValueError: Falls der Key keine Länge von 1 hat oder kein Buchstabe ist.

        >>> caesar = Caesar()
        >>> caesar.key
        >>> caesar = Caesar("a")
        >>> caesar.key
        'a'
        """
        if encryption_key and not self.check_if_key_is_valid(encryption_key):
            raise ValueError("Key muss ein Buchstabe sein und Länge 1 haben: " + str(encryption_key))
        self.key = encryption_key
        pass

    def encrypt(self, plaintext:str, key:str = None) -> str:
        """key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben wird.
        Falls kein key übergeben wird, nimmt übernimmt encrypt den Wert vom Property.

        :param plaintext: Der zu verschlüsselnde Text
        :param key: Der Verschiebewert
        :return: Der verschlüsselte Text
        :rtype: str
        :type plaintext: str
        :type key: str

        :raises ValueError: Falls kein Key gefunden werden konnte oder die Länge des Keys nicht 1 beträgt.

        >>> caesar=Caesar("b")
        >>> caesar.key
        'b'
        >>> caesar.encrypt("hallo")
        'ibmmp'
        >>> caesar.decrypt("ibmmp")
        'hallo'
        >>> caesar.encrypt("hallo", "c")
        'jcnnq'
        >>> caesar.encrypt("xyz", "c")
        'zab'
        >>> caesar.encrypt("hallo", "}")
        Traceback (most recent call last):
        ...
        ValueError: Key muss ein Buchstabe sein und Länge 1 haben: }
        """
        key = self.get_key(key).lower() # Key wird in Kleinbuchstaben umgewandelt
        if not self.check_if_key_is_valid(key):
            raise ValueError("Key muss ein Buchstabe sein und Länge 1 haben: " + str(key))

        return ''.join([chr(
            ((ord(char) + ord(key) - 2 * ord('a')) % 26)
            + ord('a')
        ) for char in plaintext])

    def decrypt(self, plaintext:str, key:str = None) -> str:
        """key ist ein Buchstabe, der definiert, um wieviele Zeichen rückwärts verschoben wird.
        Falls kein key übergeben wird, nimmt übernimmt encrypt den Wert vom Property.

        :param plaintext: Der zu entschlüsselnde Text
        :param key: Der Verschiebewert
        :return: Der entschlüsselte Text
        :rtype: str
        :type plaintext: str
        :raises ValueError: Falls kein Key gefunden werden konnte oder die Länge des Keys nicht 1 beträgt.

        >>> caesar=Caesar("b")
        >>> caesar.key
        'b'
        >>> caesar.decrypt("ibmmp")
        'hallo'
        >>> caesar.decrypt("pittw", 'i')
        'hallo'
        >>> caesar.decrypt("pittw", '}')
        Traceback (most recent call last):
        ...
        ValueError: Key muss ein Buchstabe sein und Länge 1 haben: }
        """
        key = self.get_key(key).lower() # Key wird in Kleinbuchstaben umgewandelt
        if not self.check_if_key_is_valid(key):
            raise ValueError("Key muss ein Buchstabe sein und Länge 1 haben: " + str(key))

        return self.encrypt(plaintext, chr(
            ord('a') +
            (26 - (ord(key) - ord('a'))) % 26
        ))

    def get_key(self, key:str = None):
        """Gibt den Key zurück, falls er gültig ist.
        Wird kein Key angegeben, wird der Key aus dem Property genommen.

        :param key: Der zu prüfende Key
        :return: Der Key, falls er gültig ist
        :type key: str
        :rtype: str
        :raises ValueError: Falls kein Key gefunden werden konnte

        >>> caesar=Caesar('a')
        >>> caesar.get_key()
        'a'
        >>> caesar.get_key('b')
        'b'
        """
        if not key:
            if not self.key:
                raise ValueError("Es wurde kein Key übergeben")
            return self.key
        return key

    def crack(self, crypt_text:str, elements:int = 1) -> List[str]:
        """
        berechnet eine Liste mit den wahrscheinlichsten Schlüsseln. Die Länge der Liste wird mit elements vorge-
        geben.

        :param crypt_text: Der verschlüsselte Text
        :param elements: Die Anzahl der Schlüssel, die zurückgegeben werden sollen
        :return: Eine Liste mit den wahrscheinlichsten Schlüsseln

        :rtype: List[str]
        :type crypt_text: str
        :type elements: int

        :raises ValueError: Falls elements kleiner 0 ist

        >>> caesar=Caesar()
        >>> caesar.crack("hallo", -1)
        Traceback (most recent call last):
        ...
        ValueError: elements muss größer 0 sein
        >>> str_test='Vor einem großen Walde wohnte ein armer Holzhacker mit seiner Frau und seinen zwei Kindern; das Bübchen hieß Hänsel und das Mädchen Gretel. Er hatte wenig zu beißen und zu brechen, und einmal, als große Teuerung ins Land kam, konnte er das tägliche Brot nicht mehr schaffen. Wie er sich nun abends im Bette Gedanken machte und sich vor Sorgen herumwälzte, seufzte er und sprach zu seiner Frau: "Was soll aus uns werden? Wie können wir unsere armen Kinder ernähren da wir für uns selbst nichts mehr haben?"'
        >>> caesar = Caesar()
        >>> caesar.crack(str_test)
        ['a']
        >>> caesar.crack(str_test, 100) # mehr als 26 können es nicht sein.
        ['a', 'j', 'n', 'o', 'e', 'w', 'd', 'q', 'z', 'p', 'i', 'h', 'y', 's', 'k', 'x', 'c',
         'v', 'g', 'b', 'r', 'l']
        >>> crypted = caesar.encrypt(str_test, "y")
        >>> caesar.crack(crypted, 3)
        ['y', 'h', 'l']
        """
        if elements < 1:
            raise ValueError("elements muss größer 0 sein")
        crypt_text = self.to_lowercase_letter_only(crypt_text)
        decrypted_e_frequency = {}
        # Key Verschiebung und Anzahl der e's in dem Text berechnen
        for key in string.ascii_lowercase:
            decrypted_text = self.decrypt(crypt_text, key)
            amount_of_e = Counter(decrypted_text)['e']
            decrypted_e_frequency[key] = amount_of_e

        # Sortieren der Keys nach der Anzahl der e's
        # Die Keys mit den meisten e's sind die wahrscheinlichsten
        sorted_keys = sorted(decrypted_e_frequency, key=decrypted_e_frequency.get, reverse=True)

        return sorted_keys[:min(26, elements)]

    @staticmethod
    def check_if_key_is_valid(key:str = None) -> bool:
        """Prüft, ob der key ein Buchstabe ist.
        Wird kein Key angegeben, wird der Key aus dem Property genommen.

        :param key: Der zu prüfende Key
        :return: True, falls der Key ein Buchstabe ist, sonst False
        :type key: str
        :rtype: bool

        >>> caesar=Caesar()
        >>> caesar.check_if_key_is_valid("a")
        True
        >>> caesar.check_if_key_is_valid("1")
        False
        """
        return key and key.isalpha() and len(key) == 1

    @staticmethod
    def to_lowercase_letter_only(plaintext:str) -> str:
        """Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine
        Kleinbuchstaben aus dem Bereich [a..z] sind.

        :param plaintext: Der zu bereinigende Text
        :return: Der bereinigte Text
        :rtype: str
        :type plaintext: str

        >>> caesar = Caesar()
        >>> caesar.to_lowercase_letter_only("Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine Kleinbuchstaben aus dem Bereich [a..z] sind.")
        'wandeltdenplaintextinkleinbuchstabenumundentferntallezeichendiekeinekleinbuchstabenausdembereichazsind'
        """
        return ''.join([c for c in plaintext.lower() if c.isalpha()])

if __name__ == "__main__":
    import doctest
    doctest.testmod()