def primfaktorzerlegung(n):
    faktor = 2
    faktoren = []
    while n > 1:
        while n % faktor == 0:
            faktoren.append(faktor)
            n //= faktor
        faktor += 1
    return faktoren

zahl = int(input("Gib eine Zahl ein: "))
faktoren = primfaktorzerlegung(zahl)
print("Primfaktoren:", faktoren) 