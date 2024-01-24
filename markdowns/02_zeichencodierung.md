# Codierung von Zeichen

Für eine automatisierte Verschlüsselung von Nachrichten mit dem Verschiebeverfahren ist es günstig, wenn man auf die ASCII-Codierung der Zeichen zurückgreifen kann.

Zeichen werden intern im Rechner durch Bitfolgen codiert. In Abschnitt [Exkurs - ASCII-Code](https://www.inf-schule.de/information/darstellunginformation/binaerdarstellungzeichen/exkurs_ascii) von inf-schule.de findest du die einfache und vielfach genutzte ASCII-Codierung von Zeichen.

Mithilfe der ASCII-Codierung lässt sich jedem Zeichen (aus einem vorgegebenen Zeichenvorrat) eine natürliche Zahl (aus einem passenden Zahlenbereich) zuordnen und umgekehrt. Dem Zeichen 'A' lässt sich beispielsweise nach dem ASCII-Code die Zahl 65 zuordnen.

## Fragen zur ASCII-Codierung

?[Welche Dezimalzahl ist dem Zeichen 'P' zugeordnet?]
- [ ] 77
- [x] 80
- [ ] 81

?[Welches Zeichen hat den ASCII-Code 122 (als Dezimalzahl)?]
- [ ] Z
- [x] z
- [ ] y
- [ ] x

?[In welchem Zahlenbereich liegen alle Großbuchstaben? Kreuze die Codes für 'A' und 'Z' an!]
- [ ] 63
- [x] 65
- [ ] 41
- [ ] 97
- [x] 90

## ASCII-Codierung in Python

Auf diese Zuordnung zwischen Zeichen und Zahlen kann man in Python wie folgt zugreifen. Probiere das selbst einmal aus.

```python runnable
# ord(c) wandelt das Zeichen c in den entsprechenden ASCII-Code um. 
zeichen = 'A'
zahl = ord(zeichen)
print('ord: ', zeichen, '->', zahl)

# chr(n) wandelt die Zahl n in das entsprechende Zeichen (engl. character) um.
zahl = 90
zeichen = chr(zahl)
print('chr: ', zahl, '->', zeichen)
```

Beachte, dass Zeichen in Python mit Hochkommata `'` (bzw. wahlweise Anführungszeichen `"`) dargestellt werden. Zeichen sind hier Daten vom Datentyp String.

Die vordefinierte Funktion `ord()` ordnet jedem Zeichen (gemäß ASCII-Tabelle) eine natürliche Zahl zu.

Umgekehrt ordnet die vordefinierte Funktion `chr()` (gemäß ASCII-Tabelle) einer natürlichen Zahl (aus einem bestimmten Zahlenbereich) ein Zeichen zu.

Mit diesen Hilfsfunktionen lassen sich jetzt einfache Verarbeitungsmöglichkeiten von Zeichen realisieren.


