from random import sample
from string import ascii_lowercase
 
def luo_salasana(pituus):
    kaikki = ascii_lowercase
    sana = sample(kaikki, pituus)
    return "".join(sana)
 
 
for i in range(10):
    print(luo_salasana(8))