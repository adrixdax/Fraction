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

    def __repr__(self) -> str:
        return f"Fraction({self.num}, {self.den})"

    def __str__(self) -> str:
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    def __add__(self, other: "Fraction") -> "Fraction":
        if not isinstance(other, Fraction):
            other = Fraction(other)
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)




f1 = Fraction(1, 2)
f2 = Fraction(2, 4)  # Viene semplificata automaticamente in 1/2

print(f1)       # 1/2
print(f1 + f2)  # 1