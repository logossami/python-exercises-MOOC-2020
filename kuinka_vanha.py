from datetime import datetime, timedelta
 
vaihto = datetime(1999, 12, 31)
 
paiva = int(input("Päivä: "))
kuukausi = int(input("Kuukausi: "))
vuosi = int(input("Vuosi: "))
 
s_aika = datetime(vuosi, kuukausi, paiva)
 
ero = vaihto - s_aika
 
if ero.days > 0:
    print(f"Olit {ero.days} päivää vanha, kun vuosituhat vaihtui.")
else:
    print("Et ollut syntynyt, kun vuosituhat vaihtui.")