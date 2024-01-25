from intern import verschluesseln

text = "BEISPIEL"
schluessel = 0
geheim = verschluesseln(text, schluessel)
print(geheim)
geknackt = verschluesseln(geheim, ... )
print(geknackt)