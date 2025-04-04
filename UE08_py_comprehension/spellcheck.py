__author__ = "Luka Pacar"

from typing import List, Tuple, Set


def read_all_words(filename:str) -> Set[str]:
    """
    Reads all words from a file and returns them as a set of strings.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        Set[str]: A set of words read from the file.
    """
    out = set()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            out.add(line.strip())
    return out

def split_word(wort:str) -> List[Tuple[str, str]]:
    """
    Splits a word into a list of tuples, where each tuple contains the prefix and suffix of the word.

    Args:
        wort (str): The word to split.

    Returns:
        List[Tuple[str, str]]: A list of tuples containing the prefix and suffix of the word.

    Example:
        >>> split_word('banana')
        [('', 'banana'), ('b', 'anana'), ('ba', 'nana'), ('ban', 'ana'), ('bana', 'na'), ('banan', 'a'), ('banana', '')]
    """
    out = []
    for i in range(len(wort)+1):
        out.append((wort[:i], wort[i:]))
    return out

def edit1(wort:str) -> Set[str]:
    """
    Generates a set of words that are one edit away from the given word.
    :param wort: The word to generate edits for.
    :return: A set of words that are one edit away from the given word.

    >>> set_output = edit1('abc')
    >>> set_right_output = {'abg', 'abi', 'ahc', 'kbc', 'abci', 'iabc', 'vabc', 'fbc', 'abn', 'abyc', 'pabc', 'bac', 'abnc', 'abwc', 'abv', 'albc', 'pbc', 'abcd', 'xbc', 'ybc', 'abk', 'wbc', 'abck', 'zabc', 'nabc', 'abzc', 'abcc', 'abcj', 'jabc', 'labc', 'abcz', 'arbc', 'wabc', 'abcf', 'qabc', 'mabc', 'aibc', 'avbc', 'acb', 'agbc', 'ac', 'abc', 'abbc', 'abs', 'adbc', 'aqbc', 'eabc', 'mbc', 'lbc', 'asbc', 'axc', 'abjc', 'abce', 'abxc', 'abpc', 'afc', 'abcx', 'jbc', 'ayc', 'awc', 'awbc', 'apbc', 'obc', 'abec', 'abq', 'avc', 'rabc', 'aabc', 'hbc', 'absc', 'bc', 'abh', 'amc', 'oabc', 'sabc', 'abfc', 'abp', 'ebc', 'aic', 'axbc', 'alc', 'abvc', 'abch', 'babc', 'abtc', 'fabc', 'ahbc', 'uabc', 'acc', 'aubc', 'abj', 'abt', 'abcn', 'kabc', 'abcy', 'abcg', 'habc', 'afbc', 'ambc', 'ab', 'vbc', 'aac', 'apc', 'abkc', 'abd', 'acbc', 'abb', 'akbc', 'aboc', 'abcl', 'akc', 'abqc', 'nbc', 'rbc', 'sbc', 'abca', 'ajc', 'abic', 'xabc', 'abm', 'asc', 'atc', 'cbc', 'abcq', 'abo', 'abrc', 'abgc', 'abcw', 'abcm', 'abct', 'adc', 'ibc', 'abac', 'zbc', 'abcp', 'agc', 'aebc', 'arc', 'azc', 'abz', 'aybc', 'abdc', 'cabc', 'aqc', 'abu', 'azbc', 'abl', 'abhc', 'abcr', 'abf', 'abw', 'abcu', 'tbc', 'qbc', 'abcs', 'yabc', 'aba', 'abe', 'ubc', 'anc', 'aoc', 'gbc', 'auc', 'ablc', 'dbc', 'aobc', 'abx', 'aby', 'abco', 'abcb', 'bbc', 'atbc', 'gabc', 'abuc', 'abmc', 'abcv', 'ajbc', 'aec', 'anbc', 'abr', 'dabc', 'tabc'}
    >>> set_output == set_right_output
    True
    """
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

def edit1_good(wort:str, alle_woerter:List[str]) -> Set[str]:
    """
    Generates a set of words that are one edit away from the given word and are also present in the list of all words.

    :param wort: Wort, das bearbeitet werden soll
    :param alle_woerter: Liste aller Wörter
    :return: Menge der Wörter, die ein Edit von 'wort' sind und in 'alle_woerter' enthalten sind
    """
    return edit1(wort) & set(alle_woerter)

if __name__ == '__main__':
    from doctest import testmod
    testmod()
    print(edit1_good("Pyton", list(read_all_words("de-en.txt"))))
