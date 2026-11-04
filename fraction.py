import math


class Fraction:
    def __init__(self, numerator: int, denominator: int = 1):
        if denominator == 0:
            raise ZeroDivisionError("Il denominatore non può essere zero.")

        # Gestione del segno: il meno va sempre al numeratore
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # Riduzione ai minimi termini
        gcd = math.gcd(numerator, denominator)
        self.num = numerator // gcd
        self.den = denominator // gcd

    def __add__(self, other: "Fraction") -> "Fraction":
        if not isinstance(other, Fraction):
            other = Fraction(other)
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)