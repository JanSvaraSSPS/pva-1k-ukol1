import random

nahodne_cislo = random.randint(1, 100)
pokusy = 0

while True:
    try:
        hadane_cislo = int(input("Hádej číslo od 1 do 100: "))
    except ValueError:
        print("Zadejte celé číslo.")
        continue
    if hadane_cislo < 1 or hadane_cislo > 100:
        print("Číslo musí být v rozmezí od 1 do 100.")
        continue


  
    pokusy += 1
    if hadane_cislo == nahodne_cislo:
        print(f"Uhodl jsi číslo! Počet pokusů: {pokusy}")
        
        if input("Chceš hrát znovu? (a/n): ") == "a":
            nahodne_cislo = random.randint(1, 100)
            pokusy = 0             
            continue
        else:
            break
    elif hadane_cislo < nahodne_cislo:
        print(f"Číslo je větší. Počet pokusů: {pokusy}")
    else:
        print(f"Číslo je menší. Počet pokusů: {pokusy}")