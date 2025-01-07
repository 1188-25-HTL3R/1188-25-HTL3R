# author: Luka Pacar 4CN
from typing import List

def collatz_sequence(number:int, p:int = 3) -> List[int]:
    """
    Ermittelt (rekursiv!) die Collatz-Folge für eine Zahl n.

    :param number: Die Zahl für die die Collatz-Folge ermittelt werden soll
    :param p: Der Multiplikator-Faktor für die ungeraden Zahlen. (Default = 3)
    :return: Liste mit der Collatz-Folge

    >>> collatz_sequence(13)
    [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    >>> collatz_sequence(1)
    [1]

    >>> collatz_sequence(200)
    [200, 100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    """
    if number == 1:
        return [1]
    if number % 2 == 0:
        return [number] + collatz_sequence(number // 2)
    else:
        return [number] + collatz_sequence(p * number + 1)

def longest_collatz_sequence(number: int, p:int = 3):
    """
    :param number: Startzahl
    :param p: Der Multiplikator-Faktor für die ungeraden Zahlen. (Default = 3)
    :return Startwert und Länge der längsten Collatz Zahlenfolge deren Startwert <= n ist.

    >>> longest_collatz_sequence(100)
    (97, 119)

    >>> longest_collatz_sequence(1000)
    (871, 179)

    >>> longest_collatz_sequence(10000)
    (6171, 262)

    """
    max_length = 0
    start = 0
    for i in range(1, number):
        length = len(collatz_sequence(i,p))
        if length > max_length:
            max_length = length
            start = i
    return start, max_length