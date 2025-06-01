"""
Implementierung der Elliptische-Kurven-Methode (ECM) zur Faktorisierung
Eine vereinfachte Version zur Demonstration der Grundkonzepte
"""

import random
import math
from typing import Tuple, Optional

def mod_inverse(a: int, n: int) -> int:
    """
    Berechnet das modulare Multiplikativ-Inverse von a modulo n
    Verwendet den erweiterten euklidischen Algorithmus
    """
    def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, _ = extended_gcd(a, n)
    if gcd != 1:
        raise ValueError("Modulares Inverse existiert nicht")
    return x % n

class Point:
    """Punkt auf einer elliptischen Kurve y² = x³ + ax + b"""
    def __init__(self, x: int, y: int, a: int, b: int, n: int):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.n = n

    def add(self, other: 'Point') -> Optional['Point']:
        """
        Addition zweier Punkte auf der elliptischen Kurve
        Gibt None zurück, wenn ein nicht-trivialer Faktor gefunden wurde
        """
        if self.x == other.x and self.y == other.y:
            # Verdopplung
            try:
                lam = (3 * self.x * self.x + self.a) * mod_inverse(2 * self.y, self.n) % self.n
            except ValueError:
                # GCD(2y, n) ≠ 1 bedeutet, wir haben einen Faktor gefunden
                return None
        else:
            # Addition verschiedener Punkte
            try:
                lam = (other.y - self.y) * mod_inverse(other.x - self.x, self.n) % self.n
            except ValueError:
                return None

        x3 = (lam * lam - self.x - other.x) % self.n
        y3 = (lam * (self.x - x3) - self.y) % self.n
        return Point(x3, y3, self.a, self.b, self.n)

def scalar_multiply(k: int, P: Point) -> Tuple[Optional[Point], Optional[int]]:
    """
    Skalare Multiplikation kP
    Gibt (Ergebnispunkt, gefundener_Faktor) zurück
    """
    result = P
    for _ in range(k-1):
        result = result.add(P)
        if result is None:
            # Ein Faktor wurde gefunden
            try:
                y_inv = mod_inverse(2 * P.y, P.n)
                return None, math.gcd(2 * P.y, P.n)
            except ValueError:
                return None, math.gcd(P.x - result.x, P.n)
    return result, None

def ecm_factor(n: int, B1: int = 100, B2: int = 1000, max_curves: int = 50) -> Optional[int]:
    """
    Hauptfunktion der ECM-Faktorisierung
    
    Args:
        n: Zu faktorisierende Zahl
        B1: Erste Grenze für die Glattheit
        B2: Zweite Grenze für die Glattheit
        max_curves: Maximale Anzahl zu testender Kurven
    
    Returns:
        Ein nicht-trivialer Faktor von n oder None
    """
    if n % 2 == 0:
        return 2
    
    for curve in range(max_curves):
        # Zufällige Kurvenparameter wählen
        a = random.randrange(n)
        x = random.randrange(n)
        y = random.randrange(n)
        
        # Punkt auf der Kurve erstellen
        P = Point(x, y, a, (y*y - x*x*x - a*x) % n, n)
        
        # Phase 1: Erste Glattheitsprüfung
        k = 1
        for p in range(2, B1):
            if is_prime(p):
                power = p
                while power < B1:
                    k *= p
                    power *= p
        
        Q, factor = scalar_multiply(k, P)
        if factor is not None and 1 < factor < n:
            return factor
            
        if Q is None:
            continue
            
        # Phase 2: Zweite Glattheitsprüfung (vereinfacht)
        for p in range(B1, B2):
            if is_prime(p):
                Q_new = scalar_multiply(p, Q)[0]
                if Q_new is None:
                    factor = math.gcd(p, n)
                    if 1 < factor < n:
                        return factor
    
    return None

def is_prime(n: int) -> bool:
    """Einfacher Primzahltest"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("Elliptische-Kurven-Methode (ECM) - Demonstration")
    try:
        n = int(input("Geben Sie eine zusammengesetzte Zahl ein: "))
        if n < 2:
            raise ValueError("Zahl muss größer als 1 sein")
            
        print(f"\nVersuche {n} zu faktorisieren...")
        factor = ecm_factor(n)
        
        if factor:
            print(f"\nGefundener Faktor: {factor}")
            print(f"Komplementärer Faktor: {n // factor}")
        else:
            print("\nKein Faktor gefunden. Versuchen Sie es mit anderen Parametern oder einer anderen Methode.")
            
    except ValueError as e:
        print(f"Fehler: {e}")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()
