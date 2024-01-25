from intern import verschluesseln

text = "BEISPIEL"
schluessel = 0
geheim = verschluesseln(text, schluessel)
print("Verschlüsselter Text: ", geheim)
geknackt = verschluesseln(geheim, ... )
print("Entschlüsselter Text: ", geknackt)