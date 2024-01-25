def verschieben(zeichen, schluessel):
    zahl = ord(zeichen)
    neueZahl = zahl + schluessel
    while neueZahl > ord('Z'):
        neueZahl -= 26
    neuesZeichen = chr(neueZahl)

    return neuesZeichen

def verschluesseln(text, schluessel):
    ausgabe = ""
    for c in text:
        d = verschieben(c, schluessel)
        ausgabe += d

    return ausgabe