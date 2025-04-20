__author__ = "Luka Pacar"

import functools
from math import gcd


@functools.total_ordering
class Fraction:
    """
    Diese Klasse repräsentiert einen Bruch.

    >>> Fraction(1, 2) + Fraction(1, 2)
    Fraction(1, 1)

    >>> Fraction(1, 2) - Fraction(1, 4)
    Fraction(1, 4)

    >>> Fraction(2, 3) * Fraction(3, 4)
    Fraction(1, 2)

    >>> Fraction(3, 4) / Fraction(3, 2)
    Fraction(1, 2)

    >>> -Fraction(1, 2)
    Fraction(-1, 2)

    >>> abs(Fraction(-2, 3))
    Fraction(2, 3)

    >>> ~Fraction(3, 4)
    Fraction(4, 3)

    >>> float(Fraction(1, 2))
    0.5

    >>> int(Fraction(3, 2))
    1

    >>> Fraction(7, 3).__str__()
    '2 1/3'

    >>> repr(Fraction(3, 4))
    'Fraction(3, 4)'

    >>> Fraction(1, 2) == Fraction(2, 4)
    True

    >>> Fraction(1, 3) < Fraction(1, 2)
    True

    >>> Fraction(5, 3) // Fraction(1, 2)
    3

    >>> Fraction(5, 3) % Fraction(1, 2)
    Fraction(1, 6)

    >>> Fraction(2, 3) ** 2
    Fraction(4, 9)

    >>> pow(2, Fraction(1, 2))
    1.4142135623730951

    >>> a = Fraction(1, 2)
    >>> a += Fraction(1, 2)
    >>> a
    Fraction(1, 1)

    >>> a -= Fraction(1, 4)
    >>> a
    Fraction(3, 4)

    >>> a *= 2
    >>> a
    Fraction(3, 2)

    >>> a /= 3
    >>> a
    Fraction(1, 2)

    >>> a **= 2
    >>> a
    Fraction(1, 4)

    >>> Fraction(0.75)
    Fraction(3, 4)

    >>> Fraction(Fraction(3, 4), 1)
    Fraction(3, 4)

    >>> complex(Fraction(3, 4))
    (0.75+0j)
    """
    def __init__(self, numerator, denominator = None):
        """
        Initialisiert den Bruch mit Zähler und Nenner.
        :param numerator: Der Zähler des Bruchs
        :param denominator: Der Nenner des Bruchs
        """
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def reduce(self):
        """ Kürzt den Bruch. """

        # Ist der Zähler eine Gleitkommazahl, wird diese in einen Bruch umgewandelt und mit einem Kehrwert aufgelöst
        if type(self.numerator) is not int and not isinstance(self.numerator, Fraction):
            self._numerator = self.convert_to_fraction(self.numerator)
            self.reduce()
            pass

        # Ist der Nenner eine Gleitkommazahl, wird diese in einen Bruch umgewandelt und mit einem Kehrwert aufgelöst
        if type(self.denominator) is not int and not isinstance(self.denominator, Fraction):
            self._denominator = self.convert_to_fraction(self.denominator)
            self.reduce()
            pass

        # Ist der Zähler oder Nenner ein Bruch, wird dieser immer zuerst durch einen Kehrwert aufgelöst werden
        if isinstance(self.numerator, Fraction) or isinstance(self.denominator, Fraction):
            result = self.numerator / self.denominator
            self._numerator = result.numerator
            self._denominator = result.denominator

        # Kürzen mit ganzen Zahlen
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common

        # Nenner positiv machen, falls er negativ ist (Muss man nicht unbedingt machen, aber ist schöner)
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    @property
    def numerator(self):
        """ Der Zähler des Bruchs. """
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        """ Setzt den Zähler des Bruchs. """
        self._numerator = value

    @property
    def denominator(self):
        """ Der Nenner des Bruchs. """
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        """ Setzt den Nenner des Bruchs. """
        if value is None:
            self._denominator = 1
        elif value == 0:
            raise ArithmeticError("Nenner darf nicht 0 sein")
        else:
            self._denominator = value

    @staticmethod
    def convert_to_fraction(input):
        """ Wandelt einen Wert in einen Bruch um. """
        if isinstance(input, Fraction):
            return input
        elif isinstance(input, int):
            return Fraction(input, 1)
        elif isinstance(input, float):
            result = input.as_integer_ratio()
            return Fraction(result[0], result[1])
        else:
            raise ArithmeticError("Der Wert muss ein Bruch, Integer oder Float sein")

    def __str__(self):
        """ Gibt den Bruch als String aus. """
        self.reduce()
        if self.denominator == 1:
            return str(self.numerator)
        else:
            ganze_zahl = self.numerator // self.denominator
            rest = self.numerator % self.denominator
            if ganze_zahl > 0:
                return f"{ganze_zahl} {rest.numerator}/{self.denominator}"
            else:
                return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """ Gibt den Bruch als String aus. """
        return f"Fraction({self.numerator.__repr__()}, {self.denominator.__repr__()})"

    # Vergleichsoperatoren
    def __eq__(self, other):
        """ Vergleicht zwei Brüche auf Gleichheit. """
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __lt__(self, other):
        """ Vergleicht zwei Brüche auf kleiner als. """
        return self.numerator * other.denominator < self.denominator * other.numerator

    # Unärische Operatoren
    def __neg__(self):
        """ Negiert den Bruch. """
        self.reduce()
        return Fraction(-self.numerator, self.denominator)

    def __pos__(self):
        """ Gibt den Bruch zurück. """
        self.reduce()
        return self

    def __invert__(self):
        """ Invertiert den Bruch. """
        self.reduce()
        return Fraction(self.denominator, self.numerator)

    def __abs__(self):
        """ Gibt den Betrag des Bruchs zurück. """
        self.reduce()
        return Fraction(abs(self.numerator), abs(self.denominator))

    def __complex__(self):
        """ Gibt den Bruch als komplexe Zahl zurück. """
        self.reduce()
        return complex(self.numerator / self.denominator, 0) # Realteil, Imaginärteil

    def __int__(self):
        """ Gibt den Bruch als Integer zurück. """
        self.reduce()
        return int(self.numerator / self.denominator)

    def __float__(self):
        """ Gibt den Bruch als Float zurück. """
        self.reduce()
        return float(self.numerator / self.denominator)

    def __oct__(self):
        """ Gibt den Bruch als Oktal zurück. """
        self.reduce()
        return oct(self.numerator / self.denominator)

    def __hex__(self):
        """ Gibt den Bruch als Hexadezimal zurück. """
        self.reduce()
        return hex(self.numerator / self.denominator)

    # Binäre Operatoren
    def __add__(self, other):
        """ Addiert zwei Brüche. """
        other_fraction = self.convert_to_fraction(other)
        self.reduce()
        other_fraction.reduce()
        return Fraction(self.numerator * other_fraction.denominator + self.denominator * other_fraction.numerator, self.denominator * other_fraction.denominator)

    def __radd__(self, other):
        """ Addiert zwei Brüche. """
        return self + other

    def __sub__(self, other):
        """ Subtrahiert zwei Brüche. """
        other_fraction = self.convert_to_fraction(other)
        self.reduce()
        other_fraction.reduce()
        return Fraction(self.numerator * other_fraction.denominator - self.denominator * other_fraction.numerator, self.denominator * other_fraction.denominator)

    def __rsub__(self, other):
        """ Subtrahiert zwei Brüche. """
        other_fraction = self.convert_to_fraction(other)
        self.reduce()
        other_fraction.reduce()
        return Fraction(other_fraction.numerator * self.denominator - self.numerator * other_fraction.denominator, self.denominator * other_fraction.denominator)

    def __mul__(self, other):
        """ Multipliziert zwei Brüche. """
        other_fraction = self.convert_to_fraction(other)
        self.reduce()
        other_fraction.reduce()
        return Fraction(self.numerator * other_fraction.numerator, self.denominator * other_fraction.denominator)

    def __rmul__(self, other):
        """ Multipliziert zwei Brüche. """
        return self * other

    def __truediv__(self, other):
        """ Dividiert zwei Brüche. """
        if other == 0:
            raise ArithmeticError("Division durch 0 ist nicht erlaubt")
        other_fraction = self.convert_to_fraction(other)
        self.reduce()
        other_fraction.reduce()
        return Fraction(self.numerator * other_fraction.denominator, self.denominator * other_fraction.numerator) # Kehrwert

    def __rtruediv__(self, other):
        """ Dividiert zwei Brüche. """
        if self.numerator == 0:
            raise ArithmeticError("Division durch 0 ist nicht erlaubt")
        other_fraction = self.convert_to_fraction(other)
        self.reduce()
        other_fraction.reduce()
        return Fraction(other_fraction.numerator * self.denominator, self.numerator * other_fraction.denominator) # Kehrwert

    def __floordiv__(self, other):
        """ Ganzzahldivision von zwei Brüchen. """
        if other == 0:
            raise ArithmeticError("Division durch 0 ist nicht erlaubt")
        other_fraction = self.convert_to_fraction(other)
        self.reduce()
        other_fraction.reduce()
        return self.numerator * other_fraction.denominator // self.denominator * other_fraction.numerator

    def __rfloordiv__(self, other):
        """ Ganzzahldivision von zwei Brüchen. """
        if self.numerator == 0:
            raise ArithmeticError("Division durch 0 ist nicht erlaubt")
        other_fraction = self.convert_to_fraction(other)
        self.reduce()
        other_fraction.reduce()
        return other_fraction.numerator * self.denominator // self.numerator * other_fraction.denominator

    def __mod__(self, other):
        """Modulo zweier Brüche: a % b = a - (a // b) * b"""
        if other == 0:
            raise ArithmeticError("Modulo durch 0 ist nicht erlaubt")
        other_fraction = self.convert_to_fraction(other)
        self.reduce()
        other_fraction.reduce()
        return self - (self // other_fraction) * other_fraction

    def __rmod__(self, other):
        """Modulo zweier Brüche: a % b = a - (a // b) * b"""
        if self.numerator == 0:
            raise ArithmeticError("Modulo durch 0 ist nicht erlaubt")
        other_fraction = self.convert_to_fraction(other)
        self.reduce()
        other_fraction.reduce()
        return other_fraction - (other_fraction // self) * self

    def __pow__(self, exponent):
        """ Potenzieren mit Brüchen. """
        return Fraction(self.numerator ** exponent, self.denominator ** exponent)

    def __rpow__(self, base):
        """ Potenzieren mit Brüchen. """
        return base ** float(self)

    # i* Operatoren
    def __iadd__(self, other):
        result = self + other
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

    def __isub__(self, other):
        result = self - other
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

    def __imul__(self, other):
        result = self * other
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

    def __itruediv__(self, other):
        result = self / other
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

    def __ifloordiv__(self, other):
        result = self // other
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

    def __imod__(self, other):
        result = self % other
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

    def __ipow__(self, exponent):
        result = self ** exponent
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

if __name__ == "__main__":
    import doctest
    doctest.testmod()