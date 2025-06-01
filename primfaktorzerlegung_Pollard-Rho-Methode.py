import random
import math

# Berechnet den größten gemeinsamen Teiler (ggT) von a und b
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Pollard-Rho-Algorithmus zur Faktorisierung einer Zahl n
def pollard_rho(n):
    if n % 2 == 0:  # Wenn n gerade ist, gib 2 als Faktor zurück
        return 2
    x = random.randrange(2, n)  # Zufälliger Startwert für x
    y = x                       # y startet gleich wie x
    c = random.randrange(1, n)  # Zufällige Konstante c
    d = 1                       # Anfangswert für den ggT
    while d == 1:
        # Iteriere x und y nach der Pollard-Rho-Vorschrift
        x = (pow(x, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        d = gcd(abs(x - y), n)  # Berechne ggT von |x-y| und n
        if d == n:  # Falls kein Faktor gefunden, versuche es erneut
            return pollard_rho(n)
    return d  # Gib gefundenen Nicht-Trivial-Faktor zurück

# Zerlegt eine Zahl n rekursiv in Primfaktoren
def primfaktorzerlegung(n):
    faktoren = []
    def zerlege(n):
        if n == 1:
            return
        if is_prime(n):  # Wenn n eine Primzahl ist, füge sie zur Liste hinzu
            faktoren.append(n)
            return
        faktor = pollard_rho(n)  # Finde einen Nicht-Trivial-Faktor
        zerlege(faktor)          # Zerlege den gefundenen Faktor weiter
        zerlege(n // faktor)     # Zerlege den Rest weiter
    zerlege(n)
    return sorted(faktoren)      # Gib die sortierte Liste der Primfaktoren zurück

# Prüft, ob eine Zahl n eine Primzahl ist
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Hauptroutine: Eingabe und Ausgabe
zahl = int(input("Gib eine Zahl ein: "))
faktoren = primfaktorzerlegung(zahl)
print("Primfaktoren:", faktoren)