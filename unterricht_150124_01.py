# Wiederholung if und match case
# Temparatur-Empfinden :-)
# < -10 sehr kalt
# -10 bis 5 kalt
# 5 < x < 15 mittel
# > 16 < 25 angenehm
# > 25 warm
# > 35 heiß

temp = int(input("Bitte geben Sie die Auswahl ein"))

# Bedingung mit elif
# Überprüfung, bis ein Fall eintrifft
# Danach wird der gesamte Block verlassen
# if mit elif bietet sich dann an, wenn
# Fälle untereinander sich ausschlie0en (disjunkt zueinander)
# Abhängigkeit aller Fälle untereinander
if temp <= -10:
    print("Sehr kalt")
elif temp <= 5:
    print("Kalt")
elif temp <= 15:
    print("Mittel")
elif temp <= 25:
    print("Angenehm")
elif temp <= 35:
    print("Warm")
else:
    print("Heiß")

# separate Fälle werden abgefragt
if temp <= -10:
    print("Sehr kalt")
# von -9 bis 5 [-9;5]
# logische Operatoren (and)
# Vergleichsoperatoren >, <= <
# if temp > -10 and temp <= 5:
# Aneinanderreihung von Fällen (einfache Verzweigungen)
# Geeignet für Fallabfragen, die sich überlagern
# (nicht disjunkt zueinander)
sonne = True

if -10 < temp <= 5: # Python style
    # -9, -8, ..., 5
    print("Kalt")
if 6 < temp <= 15:
    print("Mittel")
if 16 < temp <= 25:
    print("Angenehm")
if 26 < temp <= 35:
    print("Warm")
# else bezieht sich nur auf das direkt davor stehende if
if temp > 35:
    print("Heiß")

if sonne:
    print("Sonne scheint")
else:
    print("Sonne scheint nicht")

temp = 3

# match case verhält sich so wie ein if .. elif
match temp:
    case temp if temp < -10:
        print("Sehr kalt")
    case temp if -10 < temp <= 5:
        print("Kalt")
    case temp if 5 < temp <= 15:
        print("Mittel")


if -10 < temp <= 5:  # Python style
    # -9, -8, ..., 5
    print("Kalt")
if 6 < temp <= 15:
    print("Mittel")
if 16 < temp <= 25:
    print("Angenehm")
if 26 < temp <= 35:
    print("Warm")
    # else bezieht sich nur auf das direkt davor stehende if
if temp > 35:
    print("Heiß")



# if Bedingungen
# Einfache Verzweigung, Mehrfachverzweigung
# else ist eine Verzweigung mit Alternativfall

# match case:
# Auswahlmenü
# z.B. Geldautomat oder Spiel
# 1 - Geld abheben
# 2 - Geld auszahlen

# Nutzereingabe: input(), gibt die Eingabe als Zeichenkette zurück
# Konvertierung mit Funktion int() in eine Ganzzahl
x = int(input("Bitte geben Sie die Auswahl ein"))

# Fallauswahl
match x:
    # Fallunterscheidung
    case 1:
        print("Geld abheben") # Argument
        # Funktionsaufruf
    case 2:
        print("Geld auszahlen")

# String-Literal "Geld abheben"
# 2 ist int-Literal



temp = 3

# match case verhält sich so wie ein if .. elif
match temp:
    case temp if temp < -10:
        print("Sehr kalt")
    case temp if -10 < temp <= 5:
        print("Kalt")
    case temp if 5 < temp <= 15:
        print("Mittel")

print("Später")

# Bedingter Ausdruck
sonne = True
# Conditional expression ist der ternäre Operator
# ? :
print("Sonne scheint") if sonne else print("Sonne scheint nicht")

sonne = int(input("Gib ein, ob die Sonne scheint (0 = False, 1 = True)"))
ausgabe = "Sonne scheint" if sonne else "Sonne scheint nicht"
type(ausgabe) # String
print(ausgabe)


### Listen
eine_liste = [1, 9, 25]

# Von der ersten Zahl der Liste Quadratwurzel ziehen
# Wurzel mit 0.5-Potenz (^1/2)
a = eine_liste[0] ** 0.5

# Funktioniert das auch?
# Operatorenreihenfolge beachten
a = eine_liste[0] ** 1 / 2
print(a)
a = eine_liste[0] ** (1 / 2)
print(a)

# Wie schreibe ich nun in eine Liste?
# Ein vorhandenes Element ersetzen
# 1 wird zu einer 2
# Überschreiben
eine_liste[0] = 2

# Löschen und wieder einfügen
# Löscht das erste Element mit dem Wert 1
eine_liste.remove(1)
# Löscht das Element an Index 0
del eine_liste[0]
eine_liste.insert(0, 2)

# Liste initialiseren
quadratzahlen = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]

# list comprehension
# Vorteile: kürzer, schneller, Bedingungen möglich, Wiedervwendbarkeit
# generisch !
# Wie viele ausgeben?
n = int(input("Wieviele Zahlen?"))
quadratzahlen_lc = [ a**2 for a in range(1,n+1) ]
print(quadratzahlen_lc)



# Filterungen möglich
# Quadratzahlen von jeder geraden Zahl
n = int(input("Wieviele Zahlen?"))
quadratzahlen_lc = [ a**2
                     for a in range(1,n+1)
                     if a % 2 == 0 ]


# None wird immer eingefügt
quadratzahlen_lc = []
for a in range(1,n+1):
    if a % 2 == 0:
        quadratzahlen_lc.append(a**2)



quad = []
# Filterungen möglich
# Quadratzahlen von jeder geraden Zahl
n = int(input("Wieviele Zahlen?"))
quadratzahlen_lc = [ quad.append(a**2)
                     for a in range(1,n+1) if a % 2 == 0 ]

# None wird immer eingefügt
for a in range(1,n+1):
    if a % 2 == 0:
        quadratzahlen_lc.append(quad.append(a**2))

print(quadratzahlen_lc)
print(quad)


# Slicing :-)



# Filterungen möglich
# Quadratzahlen von jeder geraden Zahl
n = int(input("Wieviele Zahlen?"))
quadratzahlen_lc = [ a**2
                     for a in range(1,n+1) ]

# Slicing :-)
# [start:ende (exklsuiv):step]
# exklusiv
print(quadratzahlen_lc)
print(quadratzahlen_lc[1::2])
# Weitere Slicing Übungen
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Wir können den zweiten Doppelpunkt weglassen, wenn wir keine Schrittweite haben
# Ende immer exklusive
# Indexe von rückwärts benennen
print(quadratzahlen_lc[:-2])
print(quadratzahlen_lc[::-1])
print(quadratzahlen_lc[-1::-1])
print(quadratzahlen_lc[-1:len(quadratzahlen_lc):-1])
print(quadratzahlen_lc[-1:0:-1])
# muss leer sein, da von -1 bis -1 exklusive ausschneiden
print(quadratzahlen_lc[-1:-1:-1])

# Immutabilität
# Auf welche Datentypen ist slicing anwendbar
name = "Matthias"
name.upper()
print(name)

name = "Matthias"
name = name.upper() # vollständige Neuzuweisung erforderlich
# Referenz auf NEUEN Speicher, der alte Speicher wird aufgeräumt
print(name)

# mutable Datentyp braucht keine neue Zuweisung
# Arbeiten auf dem Original
a = [ 1,2,3]
b = a
# Zwei Türen zum selben Raum
a.append(8)
print(b)
b.append(9)
print(a)


liste = [2,3,4]
liste.append(68)
print(liste)
# [2, 3, 4, 68]


name1 = "Matthias"
name2 = "Franz"
name2 = name1
name1 = name1.upper()
# Zuweisung name2 = name1 hat KEINEN Effekt auf name1
# nach der Änderung
print(name1)
print(name2)

a = [1,2,3]
b = a
print(a is b)
# echte Kopie
c = a[:]
c[0] = 7
# Keine Auswirkung auf a
print(a)
print(c is a)

# Wie verhalten sich Tupel?
tupel = (1,2,3)
tupel = (1,2,[8,9,10])
# tupel
# (1, 2, [8, 9, 10])
print(tupel[2][1])
# 9
tupel[2][1] = 99
print(tupel)
# (1, 2, [8, 99, 10])

a = [8,9,10]
tupel(1,2,a)
# Zuweisung erfolgt auf einer Liste, nicht auf dem Tupel
tupel[2][1] = 99
print(a)
# [8, 99, 10]
b = [8,9,7]
# tupel[2] = b

# Tupel hat einen Schutz
a = 1
tupel = (1,2,a)
# Integrität des Tupels muss geschützt sein
a = "Ein String"
del a
print(tupel)


# Wie gebe ich das Einmaleins aus?

# for-Schleife
reihen = 8
faktoren = 10

for r in range(1,reihen+1):
    for faktor in range(1,faktoren+1):
        # print(f'{r}*{faktor}=' + str(r*faktor), end=' ') # macht immer einen Zeilenumbruch
        print(f'{r}*{faktor} = {r * faktor}', end=' ')
    print() # Zeilenumbruch am Ende jeder Reihe


wetter = "Kalt und nass"
# zufällig
# Was ist eine while-Schleife?
import random
# Würfeln: Zufallszahlen ziehen

# Möglichkeit 1
# Warten, bis sich das Wetter ändert
while True:
    # Verändert sich das Wetter?
    # Würfeln
    check = random.randint(1,5) # [1,2,3,4,5]
    print("Warte...")
    if check == 3:
        break

print("Endlich anderes Wetter")

# Möglichkeit 2:
# Bedingung hinter while
while random.randint(1,5) != 3: # Bedingung kann auch Funktionsaufrufe enthalten
    # Verändert sich das Wetter?
    # Würfeln
    # check = random.randint(1,5) # [1,2,3,4,5]
    print("Warte...")

while random.randint(0,4): # Bedingung kann auch Funktionsaufrufe enthalten
    # Verändert sich das Wetter?
    # Würfeln
    # check = random.randint(1,5) # [1,2,3,4,5]
    print("Warte...")

print("Endlich anderes Wetter")


# Flag-Variable zum späteren Verlassen der Schleife
bad_weather = True
# Möglichkeit 3:
# Bedingung hinter while
while bad_weather: # alles geht hier rein, was zu einem bool führt
    # Verändert sich das Wetter?
    # Würfeln
    # check = random.randint(1,5) # [1,2,3,4,5]
    if random.randint(1, 5) != 3:
        bad_weather = False
    print("Warte...")

print("Endlich anderes Wetter")


# Funktionen
# Redundanz (Wiederholung im Code vermeiden)
# benannter Block von Anweisung, der wiederverwendbar
# "Dienstleister", der für uns arbeitet
# Modularisierung, Zeitersparnis, Lokalisierung von Fehlern
# Struktur, Lesbarkeit, Übersichtlichkeit
# Wartbarkeit (an einer zentralen Stelle)
# Wie lang sollten Funktionen sein?
# Wie kann ich mein Programm effizient verteilen auf Funktionen?
# so kurz wie möglich
# Eine Funktion = Eine Aufgabe, ist Aufgabe komplex, in Teilprobleme zergliedern

# def als Schlüsselwort, dann name der Funktion, dann () als
# Parameterliste zur Eingabe
# x und y sind lokale Variablen in der Funktion
def addiere(x,y):
    # es kommt darauf an, für was der +
    # Operator definiert ist !
    print(x+y)

# x und y leben nur in der Funktion
# NameError: Bezeichner können nicht aufgelöst werden
# print(x,y)


addiere(10,5) # positionale Übergabe von Argument
# Zuordnung der Argumente an die Parameterliste erfolgt
# nach der Reihenfolge der Übergabe
# 0 wird x, 5 zu y

# Parameterübergabe per keyword Zuordnung möglich
# wie im print() und grundsätzlich auch in der Reihenfolge
# unter gewissen Voraussetzungen austauschbar
addiere(x=10, y=5) # Schlüsselwortübergabe bzw. keyword parameter
addiere(y=5, x=10)
print(5,end=' ')

addiere(8,99)
# welche Argumente kann ich an die Funktion übergeben
addiere("Hallo","Spencer")
addiere(8.5, 9.)
# Geht das auch?
addiere(.8e3,8)

addiere(str(.8e3),"k")
addiere([9.8],[1])

addiere(.8e3,"k")