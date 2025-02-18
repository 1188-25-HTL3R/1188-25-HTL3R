__author__ = "Luka Pacar"

from caeser import Caesar

class Vigenere:
    """
    Die Klasse Vigenere verschlüsselt und entschlüsselt Texte mit dem Vigenere-Verfahren.
    Der Vigenere-Algorithmus ist ein symmetrisches Verschlüsselungsverfahren, bei dem jeder Buchstabe
    des Klartextes um einen konstanten Wert verschoben wird. Der Wert wird als Schlüssel bezeichnet.
    Im Gegensatz zum Caesar-Verfahren, besteht de Schlüssel aus einem Text
    """

    def __init__(self, encryption_key:str = None):
        """
        Initialisiert die Klasse Vigenere mit einem optionalem Verschlüsselungsschlüssel.
        :param encryption_key: Der Verschlüsselungsschlüssel
        :type encryption_key: str

        :raises ValueError: Falls der Key keine Länge von 1 hat oder kein Buchstabe ist.

        >>> vigenere = Vigenere()
        >>> vigenere.key
        >>> vigenere = Vigenere("a")
        >>> vigenere.key
        'a'
        """
        if encryption_key and not self.check_if_key_is_valid(encryption_key):
            raise ValueError("Key muss nur aus Buchstaben bestehen: " + str(encryption_key))
        self.key = encryption_key
        pass

    def encrypt(self, plaintext:str, key:str = None) -> str:
        """
        Encrypted den plaintext mit dem Vigenere Algorithmus.

        key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben wird.
        Falls kein key übergeben wird, nimmt übernimmt encrypt den Wert vom Property.

        :param plaintext: Der zu verschlüsselnde Text
        :param key: Der Verschiebewert-Text
        :return: Der verschlüsselte Text
        :rtype: str
        :type plaintext: str
        :type key: str
        :raises ValueError: Falls kein Key gefunden werden konnte oder der Key nicht valide ist.

        >>> vigenere = Vigenere()
        >>> vigenere.encrypt("hello", "abcde")
        'hfnos'

        >>> vigenere.encrypt("attackatdawn", "lemon")
        'lxfopvefrnhr'

        >>> vigenere.encrypt("", "abcd")
        ''
        >>> vigenere.encrypt("hello", "ABCDE d 1 213 12")
        Traceback (most recent call last):
        ...
        ValueError: Key muss nur aus Buchstaben bestehen: abcde d 1 213 12
        """
        key = self.get_key(key).lower() # Key wird in Kleinbuchstaben umgewandelt
        if not self.check_if_key_is_valid(key):
            raise ValueError("Key muss nur aus Buchstaben bestehen: " + str(key))

        encrypted_text = ""
        for i in range(len(plaintext)):
            curr_key_part = key[i % len(key)]
            encrypted_text += Caesar.encrypt(Caesar(), plaintext[i], curr_key_part)

        return encrypted_text

    def decrypt(self, plaintext:str, key:str = None) -> str:
        """
        Decrypted den plaintext mit dem Vigenere Algorithmus.

         key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben wird.
        Falls kein key übergeben wird, nimmt übernimmt encrypt den Wert vom Property.

        :param plaintext: Der zu entschlüsselnde Text
        :param key: Der Verschiebewert-Text
        :return: Der entschlüsselte Text
        :rtype: str
        :type plaintext: str
        :raises ValueError: Falls kein Key gefunden werden konnte oder der Key nicht valide ist.

        >>> vigenere = Vigenere()
        >>> vigenere.decrypt("hfnos", "abcde")
        'hello'

        >>> vigenere.decrypt("lxfopvefrnhr", "lemon")
        'attackatdawn'

        >>> vigenere.encrypt("", "abcd")
        ''
        >>> vigenere.encrypt("hello", "ABCDE d 1 213 12")
        Traceback (most recent call last):
        ...
        ValueError: Key muss nur aus Buchstaben bestehen: abcde d 1 213 12
        """
        key = self.get_key(key).lower() # Key wird in Kleinbuchstaben umgewandelt
        if not self.check_if_key_is_valid(key):
            raise ValueError("Key muss nur aus Buchstaben bestehen: " + str(key))

        encrypted_text = ""
        for i in range(len(plaintext)):
            curr_key_part = key[i % len(key)]
            encrypted_text += Caesar.decrypt(Caesar(), plaintext[i], curr_key_part)

        return encrypted_text

    @staticmethod
    def check_if_key_is_valid(key:str = None) -> bool:
        """Prüft, ob der key nur aus Buchstaben besteht.
        Wird kein Key angegeben, wird der Key aus dem Property genommen.

        :param key: Der zu prüfende Key
        :return: True, falls der Key nur aus Buchstaben besteht, sonst False
        :type key: str
        :rtype: bool

        >>> vigenere=Vigenere()
        >>> vigenere.check_if_key_is_valid("apfel")
        True
        >>> vigenere.check_if_key_is_valid("1 apfel")
        False
        """
        return key and key.isalpha()

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

if __name__ == "__main__":
    import doctest
    doctest.testmod()

