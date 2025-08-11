guests = [" alice ", "", "Bob", "ALICE", "  bob  ", " Eve ", "eve", " ", "  ANAND"]
 
guests_main = {}
 
for guest in guests:
    name = guest.strip()
    if not name:
        continue

    caps = name.capitalize()
 
    if caps not in guests_main:
        	guests_main[caps] = len(caps)
 
print(guests_main)