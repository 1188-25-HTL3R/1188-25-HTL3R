__author__ = "Luka Pacar"

from typing import List, Tuple, Set


def read_all_words(filename:str) -> Set[str]:
    """
    Speichert alle Wörter aus einer Datei in eine Menge.

    :param filename: Der Name der Datei, die die Wörter enthält
    :return: Eine Menge aller Wörter in der Datei
    """
    out = set()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            out.add(line.lower().strip())
    return out

def split_word(wort:str) -> List[Tuple[str, str]]:
    """
    Splittet ein Wort in alle möglichen Kombinationen von Präfix und Suffix.

    :param wort: Das Wort, das gesplittet werden soll
    :return: Eine Liste von Tupeln, die das Präfix und Suffix des Wortes enthalten.

    >>> split_word('banana')
    [('', 'banana'), ('b', 'anana'), ('ba', 'nana'), ('ban', 'ana'), ('bana', 'na'), ('banan', 'a'), ('banana', '')]
    """
    wort = wort.lower()
    out = []
    for i in range(len(wort)+1):
        out.append((wort[:i], wort[i:]))
    return out

def edit1(wort:str) -> Set[str]:
    """
    Generiert eine Menge von Wörtern, die ein Edit von dem gegebenen Wort entfernt sind.
    :param wort: Das Wort, das bearbeitet werden soll
    :return: Menge der Wörter, die ein Edit von 'wort' sind

    >>> set_output = edit1('abc')
    >>> set_right_output = {'abg', 'abi', 'ahc', 'kbc', 'abci', 'iabc', 'vabc', 'fbc', 'abn', 'abyc', 'pabc', 'bac', 'abnc', 'abwc', 'abv', 'albc', 'pbc', 'abcd', 'xbc', 'ybc', 'abk', 'wbc', 'abck', 'zabc', 'nabc', 'abzc', 'abcc', 'abcj', 'jabc', 'labc', 'abcz', 'arbc', 'wabc', 'abcf', 'qabc', 'mabc', 'aibc', 'avbc', 'acb', 'agbc', 'ac', 'abc', 'abbc', 'abs', 'adbc', 'aqbc', 'eabc', 'mbc', 'lbc', 'asbc', 'axc', 'abjc', 'abce', 'abxc', 'abpc', 'afc', 'abcx', 'jbc', 'ayc', 'awc', 'awbc', 'apbc', 'obc', 'abec', 'abq', 'avc', 'rabc', 'aabc', 'hbc', 'absc', 'bc', 'abh', 'amc', 'oabc', 'sabc', 'abfc', 'abp', 'ebc', 'aic', 'axbc', 'alc', 'abvc', 'abch', 'babc', 'abtc', 'fabc', 'ahbc', 'uabc', 'acc', 'aubc', 'abj', 'abt', 'abcn', 'kabc', 'abcy', 'abcg', 'habc', 'afbc', 'ambc', 'ab', 'vbc', 'aac', 'apc', 'abkc', 'abd', 'acbc', 'abb', 'akbc', 'aboc', 'abcl', 'akc', 'abqc', 'nbc', 'rbc', 'sbc', 'abca', 'ajc', 'abic', 'xabc', 'abm', 'asc', 'atc', 'cbc', 'abcq', 'abo', 'abrc', 'abgc', 'abcw', 'abcm', 'abct', 'adc', 'ibc', 'abac', 'zbc', 'abcp', 'agc', 'aebc', 'arc', 'azc', 'abz', 'aybc', 'abdc', 'cabc', 'aqc', 'abu', 'azbc', 'abl', 'abhc', 'abcr', 'abf', 'abw', 'abcu', 'tbc', 'qbc', 'abcs', 'yabc', 'aba', 'abe', 'ubc', 'anc', 'aoc', 'gbc', 'auc', 'ablc', 'dbc', 'aobc', 'abx', 'aby', 'abco', 'abcb', 'bbc', 'atbc', 'gabc', 'abuc', 'abmc', 'abcv', 'ajbc', 'aec', 'anbc', 'abr', 'dabc', 'tabc'}
    >>> set_output == set_right_output
    True
    """
    wort = wort.lower()
    split_words = split_word(wort)
    output = set()
    for word in split_words:
        # Buchstabe fehlt
        output.add(word[0] + word[1][1:])

        # zwei Buchstaben vertauschen
        if len(word[1]) > 1:
            output.add(word[0] + word[1][1] + word[1][0] + word[1][2:])

        # Buchstaben ersetzen
        output |= {word[0] + i + word[1][1:] for i in "abcdefghijklmnopqrstuvwxyz"}


        # Buchstabe hinzufügen
        output |= {word[0] + i + word[1] for i in "abcdefghijklmnopqrstuvwxyz"}

    return output

def edit1_good(wort:str, alle_woerter:Set[str]) -> Set[str]:
    """
    Generiert eine Menge von Wörtern, die ein Edit von dem gegebenen Wort entfernt sind und auch in der Liste aller Wörter vorhanden sind.

    :param wort: Wort, das bearbeitet werden soll
    :param alle_woerter: Liste aller Wörter
    :return: Menge der Wörter, die ein Edit von 'wort' sind und in 'alle_woerter' enthalten sind
    """
    wort = wort.lower()
    return edit1(wort) & alle_woerter

def edit2_good(wort:str, alle_woerter:Set[str]) -> Set[str]:
    """
    Generiert eine Menge von Wörtern, die zwei Edits von dem gegebenen Wort entfernt sind und auch in der Liste aller Wörter vorhanden sind.
    :param wort: Wort, das bearbeitet werden soll
    :param alle_woerter: Liste aller "richtigen" Wörter
    :return: Menge der Wörter, die zwei Edits von 'wort' sind und in 'alle_woerter' enthalten sind

    >>> set_right_output = {'von', 'Pin', 'Plot', 'Pein', 'Phon', 'klon', 'Pool', 'Pony', 'Pan', 'Pylon', 'Po', 'Pol', 'Python', 'Pop', 'Prof', 'Pos'}
    >>> set_output = edit2_good('Pyon', read_all_words("de-en.txt"))
    >>> set_right_output == set_output
    True
    """
    wort = wort.lower()
    edit1_words = edit1(wort)
    edit2_words = set()
    for word in edit1_words:
        edit2_words |= edit1(word)

    return edit2_words & alle_woerter

def correct(word:str, alle_woerter:Set[str]) -> Set[str]:
    """
    Überprüft ob eine Eingabe ein Edit (max. 2 Änderungen Unterschied) von einem Wort in der Liste ist.
    :param word: Wort, das bearbeitet werden soll
    :param alle_woerter: Liste aller "richtigen" Wörter
    :return: Menge der Wörter, die ein Edit von 'wort' sind (max. 2 Änderungen Unterschied) und in 'alle_woerter' enthalten sind

    >>> woerter = read_all_words("de-en.txt")
    >>> sorted(correct("Aalsuppe", woerter))
    ['aalquappe', 'aalsuppe', 'aalsuppen']
    >>> sorted(correct("Alsuppe", woerter))
    ['aalsuppe', 'aalsuppen', 'suppe', 'ursuppe']
    >>> sorted(correct("Alsupe", woerter))
    ['aalsuppe', 'absude', 'alse', 'lupe']
    """
    word = word.lower()
    all_correct_words = set()
    edit1_words = edit1_good(word, alle_woerter)
    edit2_words = edit2_good(word, alle_woerter)

    all_correct_words |= edit1_words
    all_correct_words |= edit2_words
    if word in alle_woerter:
        all_correct_words.add(word)

    return all_correct_words


if __name__ == '__main__':
    print(sorted(correct('Alsuppe', read_all_words("de-en.txt"))))
