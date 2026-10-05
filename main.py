import random

pokusy = 0
while True:
    try:
        vybrana_obtiznost = int(input("Vyber obtížnost (1 nebo větší): "))
    except ValueError:
        print("Zadejte celé číslo.")
        continue
    if vybrana_obtiznost < 1:
        print(f"Číslo musí být větší než 1.")
        continue
    else:
        break

max_cliso_obtiznosti = vybrana_obtiznost * 100
nahodne_cislo = random.randint(1, max_cliso_obtiznosti)

while True:
    try:
        hadane_cislo = int(input(f"Hádej číslo od 1 do {max_cliso_obtiznosti}: "))
    except ValueError:
        print("Zadejte celé číslo.")
        continue
    if hadane_cislo < 1 or hadane_cislo > max_cliso_obtiznosti:
        print(f"Číslo musí být v rozmezí od 1 do {max_cliso_obtiznosti}.")
        continue
  
    pokusy += 1
    if hadane_cislo == nahodne_cislo:
        print(f"Uhodl jsi číslo! Počet pokusů: {pokusy}")
        
        if input("Chceš hrát znovu? (a/n): ").lower == "a":
            pokusy = 0  
            vybrana_obtiznost = int(input("Vyber obtížnost (1 nebo větší): "))
            max_cliso_obtiznosti = vybrana_obtiznost * 100  
            nahodne_cislo = random.randint(1, max_cliso_obtiznosti)
            continue
        else:
            break
    elif hadane_cislo < nahodne_cislo:
        print(f"Číslo je větší. Počet pokusů: {pokusy}")
    else:
        print(f"Číslo je menší. Počet pokusů: {pokusy}")
