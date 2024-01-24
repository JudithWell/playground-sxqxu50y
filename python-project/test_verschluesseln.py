import verschluesseln as p

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
    
def test_verschluesseln():
    try:
        assert p.verschluesseln('CAESAR', 26) == 'CAESAR', "Verschiebung über 'Z' hinaus funktioniert nicht!"
        
        assert p.verschluesseln('ABCDEF', 2) == 'CDEFGH', "Die Verschlüsselung von ABCDEF durch Verschiebung um 2 schlug fehl!"
        
        success()
        send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")
        
    except AssertionError as e:
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)
    
    
if __name__ == "__main__":
    test_verschluesseln()