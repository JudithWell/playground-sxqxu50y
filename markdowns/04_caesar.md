# Implementierung der Caesar-Verschlüsselung

Ziel ist es, die Verschlüsselung von Nachrichten mit dem Verschiebeverfahren ebenfalls mit einer Funktion zu realisieren.

Für die Implementierung mit einer Funktionsdefinition kann man den folgenden Algorithmus benutzen. Beachte, dass wir davon ausgehen, dass eine Nachricht nur aus den Großbuchstaben 'ABC...XYZ' besteht und Schlüssel nur positive Zahlen sind.

```
FUNKTION verschluesseln:
Parameter: text, schluessel
neuerText = ''
für alle Zeichen c in klartext:
    ermittle mit dem schluessel das zu c verschobene Zeichen d 
    füge d am Ende an die von neuerText verwaltete Zeichenkette an
Rückgabe: neuerText
```

Ergänze die Funktionsdefinition im folgenden Programmgerüst passend. Die erste Zeile importiert deine vorherige Lösung für die Methoden `verschieben()`, sodass du sie hier verwenden kannst. Du kannst dich dabei am oben angegebenen Algorithmus orientieren.

Teste auch selbst mit verschiedenen Funktionsaufrufen!

@[Verschlüsseln durch Verschiebung]({
    "stubs": ["verschluesseln.py"],
    "command": "python3 test_verschluesseln.py",
    "project": "python"
})

# Implementierung der Entschlüsselung

Texte, die mit der Funktion `verschluesseln()` verschlüsselt wurden, können mit derselben Funktion entschlüsselt werden, wenn man den Schlüssel geeignet wählt. Erprobe das mit geeigneten Beispielen!

```python runnable
from verschluesseln import verschluesseln

text = "BEISPIEL"
schluessel = 0
geheim = verschluesseln(text, schluessel)
print(geheim)
geknackt = verschluesseln(text, ... )
```

Die Entschlüsselung von Texten, die mit dem Verschiebeverfahren verschlüsselt wurden, sollen mit demselben Schlüssel entschlüsselt werden. Entwickle hierfür eine geeignete Funktion `entschluesseln()`. Du kannst dafür wieder die Methode `verschluesseln()` aufrufen!

@[Verschlüsseln durch Verschiebung]({
    "stubs": ["entschluesseln.py"],
    "command": "python3 test_entschluesseln.py",
    "project": "python"
})
