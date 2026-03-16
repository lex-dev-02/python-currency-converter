betrag = float(input("Euro Betrag "))
print("1 = PLN")
print("2 = Dollar")
print("3 = Baht")
wahl = input("Währung wählen: ")
if wahl == "1":
    ergebnis = betrag * 4.3
elif wahl == "2":
    ergebnis = betrag * 1.1
elif wahl == "3":
    ergebnis = betrag * 39
print("Ergebnis:", ergebnis)