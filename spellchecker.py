lause = input("Write text: ")
lause = lause.split()  #lause on nyt lista
 
with open("wordlist.txt") as tiedosto:
    sanalista = tiedosto.read()
    sanalista = sanalista.split()
    oikeat = []
    for sana in lause:
        if sana.lower() in sanalista:
            oikeat.append(sana)
        else:
            sana = (f"*{sana}*")
            oikeat.append(sana)
        
print(*oikeat)
 