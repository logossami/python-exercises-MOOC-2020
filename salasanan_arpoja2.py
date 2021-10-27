from random import sample, shuffle
from string import ascii_lowercase, digits, punctuation
 
def luo_hyva_salasana(pituus:int, numero, merkki):
    from random import choice
    from string import ascii_lowercase, digits, punctuation
    ssana = ''
    erikoiset = list(punctuation)
    erikoiset_osa = "!?=+-()#"
    erikoismerkit = ""
    for i in erikoiset:
        if i in erikoiset_osa:
            erikoismerkit += i
 
    while len(ssana) < pituus:
        ssana += choice(ascii_lowercase)
        if numero and len(ssana) < pituus:
            ssana += choice(digits)
        if merkki and len(ssana) < pituus:
            ssana += choice(erikoismerkit)
 
    return ssana
 
for i in range(10):
   print(luo_hyva_salasana(8, True, True))