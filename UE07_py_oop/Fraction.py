__author__ = "Luka Pacar"

class Fraction:
    """ Diese Klasse repräsentiert einen Bruch. """
    def __init__(self, numerator, denominator = None):
        """
        Initialisiert den Bruch mit Zähler und Nenner.
        :param numerator: Der Zähler des Bruchs
        :param denominator: Der Nenner des Bruchs
        """
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            raise ValueError("Der Nenner darf nicht null sein.")
        if not denominator:
            self.denominator = 1

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
        return self._numerator

    @denominator.setter
    def denominator(self, value):
        """ Setzt den Nenner des Bruchs. """
        self._numerator = value

    # Vergleichsoperatoren
    def __eq__(self, other):
        """ Vergleicht zwei Brüche auf Gleichheit. """
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other):
        """ Vergleicht zwei Brüche auf Ungleichheit. """
        return not self == other

    def __lt__(self, other):
        """ Vergleicht zwei Brüche auf kleiner als. """
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other):
        """ Vergleicht zwei Brüche auf kleiner gleich. """
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other):
        """ Vergleicht zwei Brüche auf größer als. """
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other):
        """ Vergleicht zwei Brüche auf größer gleich. """
        return self.numerator * other.denominator >= self.denominator * other.numerator

    # Unärische Operatoren
    def __neg__(self):
        """ Negiert den Bruch. """
        return Fraction(-self.numerator, self.denominator)

    def __pos__(self):
        """ Gibt den Bruch zurück. """
        return self

    def __invert__(self):
        """ Invertiert den Bruch. """
        return Fraction(self.denominator, self.numerator)

    def __abs__(self):
        """ Gibt den Betrag des Bruchs zurück. """
        return Fraction(abs(self.numerator), abs(self.denominator))

    def __complex__(self):
        """ Gibt den Bruch als komplexe Zahl zurück. """
        return complex(self.numerator, self.denominator)

    def __int__(self):
        """ Gibt den Bruch als Integer zurück. """
        return int(self.numerator / self.denominator)

    def __float__(self):
        """ Gibt den Bruch als Float zurück. """
        return float(self.numerator / self.denominator)

    def oct(self):
        """ Gibt den Bruch als Oktal zurück. """
        return oct(self.numerator / self.denominator)

    def hex(self):
        """ Gibt den Bruch als Hexadezimal zurück. """
        return hex(self.numerator / self.denominator)

    # Binäre Operatoren
    def __add__(self, other):
        """ Addiert zwei Brüche. """
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator)

    def __sub__(self, other):
        """ Subtrahiert zwei Brüche. """
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator)

    def __mul__(self, other):
        """ Multipliziert zwei Brüche. """
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        """ Dividiert zwei Brüche. """
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator) # Kehrwert

    def __floordiv__(self, other):
        """ Ganzzahldivision von zwei Brüchen. """
        return Fraction(self.numerator * other.denominator // self.denominator * other.numerator)

    def __mod__(self, other):
        """Modulo zweier Brüche: a % b = a - (a // b) * b"""
        if other == 0:
            raise ZeroDivisionError("Modulo durch 0 ist nicht erlaubt")
        return self - (self // other) * other

    def __pow__(self, exponent):
        if isinstance(exponent, int):
            return Fraction(self.numerator ** exponent, self.denominator ** exponent)
        else:
            raise TypeError("Exponent muss ganzzahlig sein")

    def __lshift__(self, shift):
        # Sicherstellen, dass der Bruch einen Integer ergibt
        if self.numerator % self.denominator == 0:
            return Fraction(self.numerator << shift, self.denominator)
        else:
            raise ValueError("Der Bruch kann nicht verschoben werden, da er keinen ganzzahligen Wert ergibt.")

    def __rshift__(self, shift):
        # Sicherstellen, dass der Bruch einen Integer ergibt
        if self.numerator % self.denominator == 0:
            return Fraction(self.numerator >> shift, self.denominator)
        else:
            raise ValueError("Der Bruch kann nicht verschoben werden, da er keinen ganzzahligen Wert ergibt.")

    # Reflection Operatoren
    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return Fraction(other * self.denominator - self.numerator, self.denominator)

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        return Fraction(other * self.denominator, self.numerator)

    def __rfloordiv__(self, other):
        return Fraction(other * self.denominator // self.numerator, 1)

    def __rmod__(self, other):
        return Fraction(other * self.denominator % self.numerator, self.denominator)

    def __rpow__(self, exponent):
        return Fraction(exponent ** self.numerator, self.denominator ** exponent)

    # Shift Operationen wo der Bruch der Shift ist, macht keinen Sinn

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

    def __ilshift__(self, shift):
        result = self << shift
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self

    def __irshift__(self, shift):
        result = self >> shift
        self.numerator = result.numerator
        self.denominator = result.denominator
        return self
