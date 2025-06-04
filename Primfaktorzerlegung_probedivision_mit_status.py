import time

def primfaktorzerlegung(n):
    faktor = 2
    faktoren = []
    max_faktor = int(n ** 0.5) + 1
    last_update = time.time()
    
    print(f"Starte Primfaktorzerlegung für {n}...")
    while n > 1:
        current_time = time.time()
        if current_time - last_update >= 0.5:
            progress = (faktor / max_faktor) * 100
            print(f"\rFortschritt: {min(progress, 99.9):.1f}% - Aktueller Faktor: {faktor}", end="")
            last_update = current_time
            
        while n % faktor == 0:
            faktoren.append(faktor)
            n //= faktor
            
        faktor += 1
        if faktor > max_faktor and n > 1:
            faktoren.append(n)
            print(f"\rGroße Primzahl gefunden: {n}")
            break
    
    print("\nFertig!")
    return faktoren

zahl = int(input("Gib eine Zahl ein: "))
faktoren = primfaktorzerlegung(zahl)
print("Primfaktoren:", faktoren) 