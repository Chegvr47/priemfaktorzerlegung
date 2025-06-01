# Komplexität bei der Primfaktorzerlegung

## Was bedeutet Komplexität?
Die Komplexität beschreibt, wie der Rechenaufwand (Zeit) und Speicherbedarf mit der Größe der Eingabe wächst.

## Vergleich der Algorithmen

### 1. Naive Methode (Trial Division)
- **Zeitkomplexität: O(√n)**
  - Bedeutet: Die Laufzeit wächst mit der Quadratwurzel der Eingabezahl
  - Beispiel: Für eine 100-stellige Zahl ≈ 10⁵⁰ Operationen
- **Speicherkomplexität: O(1)**
  - Konstanter Speicherbedarf
  - Unabhängig von der Eingabegröße

### 2. Pollard-Rho-Methode
- **Zeitkomplexität: O(n^1/4)**
  - Bedeutet: Die Laufzeit wächst mit der vierten Wurzel der Eingabezahl
  - Deutlich schneller als Trial Division
  - Beispiel: Für eine 100-stellige Zahl ≈ 10²⁵ Operationen
- **Speicherkomplexität: O(1)**
  - Konstanter Speicherbedarf
  - Sehr speichereffizient

### 3. Quadratisches Sieb (QS)
- **Zeitkomplexität: O(e^(√(ln n * ln ln n)))**
  - Subexponentieller Algorithmus
  - Derzeit schnellster bekannter Algorithmus für Zahlen bis ~100 Stellen
  - Beispiel: Für eine 100-stellige Zahl deutlich weniger als 10²⁵ Operationen
- **Speicherkomplexität: O(e^(√(ln n * ln ln n)/2))**
  - Wächst subexponentiell
  - Benötigt signifikant mehr Speicher als die anderen Methoden

## Praktische Bedeutung

### Für kleine Zahlen (< 10⁶)
- Naive Methode ist ausreichend
- Einfache Implementierung
- Geringer Speicherbedarf

### Für mittlere Zahlen (20-40 Stellen)
- Pollard-Rho ist optimal
- Guter Kompromiss zwischen Geschwindigkeit und Implementierungsaufwand
- Minimaler Speicherbedarf

### Für große Zahlen (> 50 Stellen)
- Quadratisches Sieb oder modernere Verfahren notwendig
- Hoher Implementierungsaufwand
- Bedeutender Speicherbedarf
- Parallelisierung oft notwendig

## Bedeutung für die Kryptographie
- RSA-Verschlüsselung basiert auf der Schwierigkeit der Primfaktorzerlegung
- Aktuelle RSA-Schlüssel: 2048-4096 Bit (≈ 617-1234 Dezimalstellen)
- Selbst mit besten Algorithmen praktisch nicht in akzeptabler Zeit faktorisierbar
- Quantencomputer könnten dies ändern (Shor-Algorithmus)

## Visualisierung der Komplexität
```
Größenordnung der Operationen für eine n-stellige Zahl:

Naive Methode:      O(10^(n/2))
Pollard-Rho:        O(10^(n/4))
Quadratisches Sieb: O(e^(√(n * ln(n))))
```

## Fazit
Die Wahl des Algorithmus hängt ab von:
1. Größe der zu faktorisierenden Zahl
2. Verfügbarem Speicher
3. Anforderungen an die Laufzeit
4. Implementierungsaufwand
