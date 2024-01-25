from intern import verschluesseln
from entschluesseln import entschluesseln

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
    
def test_entschluesseln():
    try:
        text = "ABCDEF"
        schluessel = 5
        geheim = verschluesseln(text, schluessel)
        assert entschluesseln(geheim, schluessel) == verschluesseln(geheim, -schluessel), "Entschlüsselung fehlgeschlagen!"
        
        success()
        send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")
        
    except AssertionError as e:
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)
    
    
if __name__ == "__main__":
    test_entschluesseln()