import verschieben as p

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
    
def test_verschieben():
    try:
        assert p.verschieben('B', 12) == 'N', "'B' um 12 verschieben hat nicht geklappt!"
        
        assert p.verschieben('A', 26) == 'A', "'A' um 26 verschieben hat nicht geklappt!"
        
        assert p.verschieben('S', 15) == 'H', "'H' um 15 verschieben hat nicht geklappt!"
        
        success()
        send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")
        
    except AssertionError as e:
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)
        send_msg("Tipp 💡", "Denk daran, wie in der vorherigen Aufgabe den 'Wertebereich' auf Buchstaben zwischen A und Z zu beschränken!")
    
    
if __name__ == "__main__":
    test_verschieben()