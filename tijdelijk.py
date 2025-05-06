prijzen={
    "aardbei":"3.0",
    "vanille":"4.0",
    "chocolade":"5.0"
}
aanbieding=float(prijzen["aardbei"]) *0.8
reclame_tekst=(f"Vandaag in de aanbieding: vanille-ijs, 1 liter € {aanbieding}")
reclame_tekst2=reclame_tekst[:52]
reclame_tekst3=reclame_tekst2.upper()
reclame_tekst4=reclame_tekst3.split(" ")
for el in reclame_tekst4:
    if len(el)>4:
        print(el.upper())
    else:
        print(el.lower())
        












