# Phase 1: Recherche zur Primfaktorzerlegung

## Vergleichende Übersicht der Algorithmen

| Algorithmus | Zeitkomplexität | Speicherkomplexität | Optimale Anwendung | Besonderheiten |
|------------|-----------------|---------------------|-------------------|----------------|
| Naive Methode (Trial Division) | O(√n) | O(1) | Zahlen < 10⁶ | Einfach implementierbar, deterministisch |
| Pollard-Rho | O(n^1/4) | O(1) | 20-40 Dezimalstellen | Probabilistisch, effizient für kleine Faktoren |
| Quadratisches Sieb | O(e^(√(ln n * ln ln n))) | O(e^(√(ln n * ln ln n)/2)) | Bis ~100 Dezimalstellen | Effizient für große Zahlen, hoher Speicherbedarf |
| Zahlkörpersieb | O(exp((64/9)^(1/3) * (ln n)^(1/3) * (ln ln n)^(2/3))) | O(exp((32/9)^(1/3) * (ln n)^(1/3) * (ln ln n)^(2/3))) | > 100 Dezimalstellen | Aktuell schnellster Algorithmus für sehr große Zahlen |
| Elliptische Kurven | O(exp(√(2 ln p ln ln p))) | O(ln n) | Mittlere Faktoren | Effektiv für spezielle Faktorgrößen |

## 1. Algorithmen Recherche

### 1.1 Naive Methode (Trial Division)

#### Funktionsweise
- Systematisches Testen aller möglichen Teiler bis zur Wurzel der Zahl
- Schrittweise Division durch Primzahlen (2, 3, 5, 7, ...)
- Bei erfolgreicher Division: Faktor gefunden und Prozess wird mit dem Quotienten wiederholt
- Fortsetzung bis keine weiteren Faktoren gefunden werden können

#### Komplexität
- Zeitkomplexität: O(√n)
- Grund: Prüfung aller Zahlen bis zur Wurzel der Eingabezahl
- Speicherkomplexität: O(1) - konstanter Speicherbedarf

#### Vor- und Nachteile
Vorteile:
- Einfache Implementierung
- Garantiert korrekte Ergebnisse
- Gut für kleine Zahlen (< 10⁶)
- Didaktisch wertvoll zum Verständnis

Nachteile:
- Sehr ineffizient für große Zahlen
- Exponentieller Anstieg der Rechenzeit
- Ungeeignet für kryptographische Anwendungen

#### Implementierungsdetails
- Optimierung durch Prüfung nur ungerader Zahlen nach 2
- Verwendung einer Primzahlenliste für effizientere Teilertests
- Mögliche Parallelisierung der Teilersuche
- Abbruchbedingung: Wenn keine Teiler ≤ √n gefunden wurden

### 1.2 Pollard-Rho-Methode

#### Funktionsweise und mathematischer Hintergrund
- Basiert auf dem "Geburtstagsproblem" der Wahrscheinlichkeitstheorie
- Verwendet eine Pseudozufallsfunktion f(x) = (x² + c) mod n
- Erzeugt eine Sequenz von Zahlen: x₁, x₂, x₃, ...
- Sucht nach Kollisionen in der Sequenz (Floyd's Cycle-Finding Algorithm)
- Wenn xᵢ ≡ xⱼ (mod p), dann ist p ein Faktor von n

#### Komplexität
- Zeitkomplexität: O(n^1/4) im Durchschnitt
- Deutlich schneller als die naive Methode
- Speicherkomplexität: O(1) - benötigt nur konstanten Speicher
- Monte-Carlo-Algorithmus: Probabilistische Erfolgswahrscheinlichkeit

#### Implementierungsdetails
- Wahl der Konstante c (meist c = 1)
- Floyd's Cycle-Finding:
  - Tortoise and Hare Algorithmus
  - Schneller Zeiger (2 Schritte) und langsamer Zeiger (1 Schritt)
- GCD-Berechnung für Faktorfindung
- Abbruchkriterien und Neustart bei Misserfolg

#### Anwendungsfälle
- Mittelgroße Zahlen (etwa 20-40 Dezimalstellen)
- Effektiv bei Zahlen mit kleinen Primfaktoren
- Wichtiger Baustein in der Faktorisierung großer Zahlen
- Parallelisierbar durch verschiedene Startwerte

### 1.3 Quadratisches Sieb (QS)

#### Mathematische Grundlagen
- Basiert auf der Fermat-Faktorisierung: n = x² - y²
- Sucht nach Zahlen Q(x) = x² - n, die sich vollständig faktorisieren lassen
- Verwendet eine Faktorbasis aus kleinen Primzahlen
- Nutzt lineare Algebra über GF(2) zur Findung von Quadraten
- Siebt effizient große Mengen von Q(x)-Werten

#### Komplexität
- Zeitkomplexität: O(e^(√(ln n * ln ln n)))
- Derzeit schnellster bekannter Algorithmus für Zahlen bis ~100 Dezimalstellen
- Speicherkomplexität: O(e^(√(ln n * ln ln n)/2))
- Deutlich effizienter als Pollard-Rho für große Zahlen

#### Implementierungsherausforderungen
- Wahl der optimalen Faktorbasis-Größe
- Effiziente Implementierung des Siebprozesses
- Matrix-Operationen über GF(2)
- Speichermanagement bei großen Zahlen
- Parallelisierung der Berechnungen

#### Optimierungsmöglichkeiten
- Multiple Polynome (MPQS)
- Self-Initializing Quadratic Sieve (SIQS)
- Large Prime Variation
- Parallelisierung auf mehreren Systemen
- GPU-Beschleunigung für Matrix-Operationen

### 1.4 Moderne Verfahren

#### 1.4.1 Zahlkörpersieb (Number Field Sieve, NFS)
##### Funktionsweise
- Weiterentwicklung des Quadratischen Siebs
- Nutzt algebraische Zahlkörper für die Faktorisierung
- Basiert auf speziellen polynomiellen Kongruenzen
- Verwendet zwei verschiedene Siebprozesse (rational und algebraisch)

##### Komplexität
- Zeitkomplexität: O(exp((64/9)^(1/3) * (ln n)^(1/3) * (ln ln n)^(2/3)))
- Derzeit schnellster bekannter Algorithmus für Zahlen > 100 Stellen
- Speicherkomplexität: O(exp((32/9)^(1/3) * (ln n)^(1/3) * (ln ln n)^(2/3)))

##### Besonderheiten
- Sehr komplexe Implementierung
- Hoher Speicherbedarf
- Optimal für sehr große Zahlen (> 100 Stellen)
- Wird für Rekorde in der Faktorisierung verwendet

#### 1.4.2 Elliptische-Kurven-Methode (ECM)
##### Funktionsweise
- Basiert auf der Arithmetik elliptischer Kurven
- Nutzt Punktaddition auf elliptischen Kurven
- Sucht nach glatten Zahlen in der Gruppenordnung
- Kann gezielt kleine Faktoren finden

##### Komplexität
- Zeitkomplexität: O(exp(√(2 ln p ln ln p))) für kleinsten Primfaktor p
- Subexponentielle Laufzeit
- Speicherkomplexität: O(ln n)
- Besonders effizient für Zahlen mit mittelgroßen Primfaktoren

##### Anwendungen
- Zwischenschritt in mehrstufigen Faktorisierungen
- Effektiv bei Zahlen mit Faktoren mittlerer Größe
- Parallelisierbar auf vielen Computern
- Wichtig in der Kryptanalyse

#### 1.4.3 Aktuelle Forschung
##### Quantenalgorithmen
- Shor-Algorithmus: Polynomielle Laufzeit auf Quantencomputern
- Theoretische Bedrohung für RSA
- Praktische Implementierung noch nicht möglich

##### Hybride Ansätze
- Kombination verschiedener Algorithmen
- Automatische Methodenwahl
- Verteilte Berechnungen
- Cloud-Computing-Ansätze

##### Neue Entwicklungen
- Verbesserungen des Zahlkörpersiebs
- Speichereffiziente Varianten
- Parallelisierungsstrategien
- Hardware-Optimierungen (FPGAs, GPUs)

## 2. Wissenschaftliche Quellen

### 2.1 Primärquellen (mindestens 3)
- Akademische Paper
- Fachbücher
- Wissenschaftliche Websites
- Konferenzberichte

### 2.2 Dokumentation
- Quellenangaben nach wissenschaftlichem Standard
- Kurzzusammenfassungen
- Relevante Zitate

## 3. Netzwerksicherheit

### 3.1 RSA-Verschlüsselung
- Grundprinzip
- Bedeutung der Primfaktorzerlegung
- Aktuelle Schlüssellängen

### 3.2 Sicherheitsrelevanz
- Angriffsmöglichkeiten
- Verteidigungsstrategien
- Zukunftsperspektiven

### 3.3 Praxisbeispiele
- Erfolgreiche Angriffe
- Präventionsmaßnahmen
- Best Practices

## 4. Recherche-Dokumentation

### 4.1 Zusammenfassung
- Wichtigste Erkenntnisse
- Vergleich der Methoden
- Offene Fragen

### 4.2 Vorbereitung Phase 2
- Notwendige Bibliotheken
- Testdaten
- Implementierungsplan

## Timeline
- Tag 1: Algorithmen und mathematische Grundlagen
- Tag 2: Netzwerksicherheit und Quellensammlung
