# author: Luka Pacar 4CN
from time import time


def mc_carthy(n:int, current_depth:int = 0) -> list[int]:
    """
    Ermittelt die McCarthy-Funktion für eine Zahl n.

    :param n: Die Zahl für die die McCarthy-Funktion ermittelt werden soll
    :param current_depth: Die aktuelle maximale Rekursionstiefe
    :return: Wert der McCarthy-Funktion

    >>> mc_carthy(100)
    [91, 1]

    >>> mc_carthy(91)
    [91, 10]

    >>> mc_carthy(50)
    [91, 14]

    """
    if n > 100:
        return [n - 10, current_depth]
    else:
        first_recursion = mc_carthy(n + 11, current_depth + 1)
        second_recursion = mc_carthy(first_recursion[0], current_depth + 1)
        return [second_recursion[0], max(first_recursion[1], second_recursion[1])]

if __name__ == "__main__":
    m_list = [mc_carthy(i) for i in range(0, 200)]
    t0 = time()
    m_dict = {mc_carthy(i, -1)[0]:i for i in range(0, 200)}
    # Bei dem Dictionary werden Key-Duplikate überschrieben, daher sind die ersten 100 Werte nicht mehr vorhanden
    print(m_dict)
    print("Time:", (time() - t0) * 1000.0, "ms")
