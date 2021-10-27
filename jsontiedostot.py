import json
 
def tulosta_henkilot(tiedosto:str):
 
    with open (tiedosto) as tiedosto:
 
        data = tiedosto.read()
        opiskelijat = json.loads(data)
        
    for opiskelija in opiskelijat:
        lista = opiskelija["harrastukset"]
        yhd = ""
        for alkio in lista:
            alkio.replace("\n", "")
            yhd = ", ".join(lista)
 
        print(f'{opiskelija["nimi"]} {opiskelija["ika"]} vuotta ({yhd})')
 
tulosta_henkilot("tiedosto1.json")