# author: Luka Pacar 4CN

def is_palindrom(word:str):
    """
    Schaut ob ein Wort ein Palindrom ist

    :param word: Das Wort das überprüft werden soll
    """
    word = word.lower()
    return word == word[::-1]

def is_palindrom_sentence(s:str):
    """
    Schaut ob ein Satz ein Palindrom ist.
    Dabei werden Satzzeichen und Leerzeichen ignoriert.

    :param s: Der Satz der überprüft werden soll

    >>> is_palindrom_sentence("Was it a car or a cat I saw?")
    True

    >>> is_palindrom_sentence("A Santa lived as a devil at NASA.")
    True

    >>> is_palindrom_sentence("Once upon a time.")
    False
    """
    s = ''.join(e for e in s if e.isalnum()).lower() # Filtert Satzzeichen und Leerzeichen (Nicht Alphamnumerische Zeichen)
    return is_palindrom(s)

def palindrom_product(x):
    """
    Ermittelt die größte Palindromzahl (kleiner als x), die das Produkt von zwei 3-stelligen Zahlen ist.

    :param x: Die Zahl bis zu der die Produkte ermittelt werden sollen

    >>> palindrom_product(1000000)
    906609

    >>> palindrom_product(100000)
    99999

    >>> palindrom_product(1)
    -1
    """

    palindrom = -1
    for i in range(100, 999):
        for j in range(100, 999):
            product = i * j
            if product < x and is_palindrom(str(product)):
                # Math max in python
                palindrom = max(palindrom, product)

    return palindrom

def to_base(number:int, base:int) -> str:
    """
    Konvertiert eine Zahl in eine andere Basis

    :param number: Zahl im 10er-System
    :param base: Zielsystem (maximal 36)
    :return Die Zahl im Zielsystem

    >>> to_base(10, 2)
    '1010'

    >>> to_base(10, 16)
    'A'

    >>> to_base(10, 10)
    '10'
    """
    if base > 36:
        raise ValueError("Base must be less than or equal to 36")
    if number == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result

def get_dec_hex_palindrom(x):
    """
    Ermittelt die größte Zahl (kleiner als x) die sowohl im Dezimalsystem als auch im Hexadezimalsystem ein Palindrom ist.

    :param x: Die Zahl bis das Ergebnis hin-iterieren darf

    >>> get_dec_hex_palindrom(1000)
    979

    >>> get_dec_hex_palindrom(1000000)
    845548

    >>> get_dec_hex_palindrom(1)
    -1
    """
    palindrom = -1
    for i in range(1, x):
        if is_palindrom(str(i)) and is_palindrom(to_base(i, 16)): # hex(i) gibt 0x... zurück, daher [2:] um die ersten beiden Zeichen zu entfernen
            palindrom = max(i, palindrom)

    return palindrom