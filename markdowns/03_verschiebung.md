# Ein Programm zur Buchstabenverschiebung

Die Buchstabenverschiebung lässt sich in Python sehr leicht mit Hilfe der Funktionen `ord()` und `chr()` realisieren.

```python runnable
zeichen = 'P'
schluessel = 7
zahl = ord(zeichen)
neueZahl = zahl + schluessel
neuesZeichen = chr(neueZahl)
print(neuesZeichen)
```

**Wir beschränken uns im Folgenden auf die Codierung von Großbuchstaben.**

### Aufgabe 1:

a. Das Python-Programm zur Buchstabenverschiebung funktioniert nicht richtig, wenn man z.B. `zeichen = 'T'` und `schluessel = 10` vorgibt. Teste und begründe.

*Hinweis:* Vielleicht hilft ein weiterer Blick in die [ASCII-Tabelle](https://www.inf-schule.de/information/darstellunginformation/binaerdarstellungzeichen/exkurs_ascii)

b. Ändere das Python-Programm zur Buchstabenverschiebung so ab, dass es für alle sinnvollen Vorgaben `zeichen = ...` und `schluessel = ...` korrekt funktioniert.

**Überprüfe selbst, ob das Programm korrekt funktioniert!**

::: *Hinweis:* 
Die `neueZahl` liegt außerhalb des Wertebereichs der Großbuchstaben. Das entspricht einer Verschiebung über den Buchstaben 'Z' hinaus, also z.B. von 'T' auf 'D'.

Hier ist eine weitere "Verschiebung" zurück in den Wertebereich erforderlich.

Programmiere also: Wenn/Solange `neueZahl` nicht im Wertebereich liegt, reduziere `neueZahl` um 26.

Warum 26? Weil wir vom Ende des Alphabets wieder an den Anfang wollen. Sind wir auf "dem Buchstaben hinter Z", wollen wir auf A zurück, usw. 
:::

# Eine Funktion zur Buchstabenverschiebung

Beim Verschiebeverfahren wird jedem Buchstaben des (Großbuchstaben-) Alphabets ein verschobener Buchstabe zugeordnet. Für die Zuordnung muss zusätzlich die Verschiebezahl als Schlüssel vorgegeben werden.

Wir beschreiben das Verhalten dieser Buchstabenverschiebung mit einer Funktion `verschieben(zeichen, schluessel)`.

*Füge in die untere Definition deinen Code aus dem vorherigen Programmfeld ein und überprüfe, ob die Verschiebung korrekt funktioniert!*

@[Funktion zur Buchstabenverschiebung]({"stubs": ["verschieben.py"], "command": "python3 test_verschieben.py", "project": "python"})

