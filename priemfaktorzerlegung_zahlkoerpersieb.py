# Quadratisches Sieb (Quadratic Sieve) - stark vereinfachte Version für kleine Zahlen
# Hinweis: Für große Zahlen ist das Verfahren deutlich komplexer und benötigt viele Optimierungen!

import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_square(n):
    return int(math.isqrt(n)) ** 2 == n

def quadratic_sieve(n):
    # Schritt 1: Wähle eine kleine Faktorbasis (Primzahlen <= 20)
    factor_base = [2, 3, 5, 7, 11, 13, 17, 19]
    # Schritt 2: Suche B-Zahlen x, so dass x^2 mod n B-faktorisierbar ist
    xlist = []
    qxlist = []
    sqrt_n = int(math.isqrt(n)) + 1
    for i in range(0, 30):  # Suche 30 Kandidaten
        x = sqrt_n + i
        qx = x * x - n
        orig_qx = qx
        factors = []
        for p in factor_base:
            while qx % p == 0:
                qx //= p
                factors.append(p)
        if abs(qx) == 1:  # Vollständig faktorisierbar
            xlist.append(x)
            qxlist.append(orig_qx)
        if len(xlist) >= len(factor_base) + 1:
            break
    # Schritt 3: Suche zwei Mengen, deren Produkt ein Quadrat ist (hier: einfach zwei gleiche nehmen)
    for i in range(len(xlist)):
        for j in range(i+1, len(xlist)):
            a = xlist[i] * xlist[j]
            b = math.isqrt(abs(qxlist[i] * qxlist[j]))
            if b * b == abs(qxlist[i] * qxlist[j]):
                # Schritt 4: Berechne ggT(a-b, n)
                factor = gcd(abs(a - b), n)
                if 1 < factor < n:
                    return factor, n // factor
    return None

# Beispielnutzung
n = int(input("Gib eine Zahl ein: "))
result = quadratic_sieve(n)
if result:
    print(f"Nicht-triviale Faktoren von {n} sind: {result[0]} und {result[1]}")
else:
    print("Keine Faktoren gefunden (oder Zahl ist zu groß/ungeeignet für diese Demo).")