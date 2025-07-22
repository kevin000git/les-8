def mijn_functie_2():
    pass
def aanbieding_1():
    return {
        "smaak": "aardbei",
        "prijs": 4,  # prijs in euro's
        "korting": (4) * 0.9  # 10% korting
    }

aanbieding_1 = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {aanbieding_1()['smaak']}, van {aanbieding_1()['prijs']:.2f} euro voor {aanbieding_1()['korting']:.2f} euro."


print (aanbieding_1)

#inkomsten_totaal():
inkomsten_totaal_1 = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")
maandag = 220
dinsdag = 430
woensdag = 125
donderdag = 160
vrijdag = 205
zaterdag = 90
zondag = 345
inkomsten_totaal_1 = (maandag + dinsdag + woensdag + donderdag + vrijdag + zaterdag + zondag)


inkomsten_totaal_1 = (maandag, dinsdag, woensdag, donderdag, vrijdag, zaterdag, zondag)



totaal = int(maandag) + int(dinsdag) + int(woensdag) + int(donderdag) + int(vrijdag) + int(zaterdag) + int(zondag)
print ("totaal bedrag van de week:",totaal)

bedrag = totaal * 0.09  # 9% btw
string_inkomsten = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."

print (string_inkomsten)

#laag_hoog():
nummers = [int(maandag), int(dinsdag), int(woensdag), int(donderdag), int(vrijdag), int(zaterdag), int(zondag)]
laag = min(nummers)
hoog = max(nummers)
for i in range(len(nummers)):
    if nummers[i] == laag:
        laag = nummers[i]
    if nummers[i] == hoog:
        hoog = nummers[i]

print ("minst goede dag:", laag)
print ("beste dag:", hoog)

#gemiddelde():
gemiddelde = totaal / 7

string_gemiddelde = f"Het gemiddelde van de week is {gemiddelde:.2f} euro."
print (string_gemiddelde)

#hoog_laag():
hoog_laag = f"De hoogste omzet was {hoog} euro op een {nummers.index(hoog) + 1}. De laagste omzet was {laag} euro op een {nummers.index(laag) + 1}."
print(hoog_laag)


