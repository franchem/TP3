"""
Par Mika Franche
2025/09/11
Dungeon Crawler vraiment nul
"""
import random
import random as rd
vies = 20
victoires, defaites = 0, 0
count, combats = 0, 0
consecutives = 0


while vies > 0:
    count += 1
    force = rd.randint(1, 10)
    if count == 3:
        force = random.randint(8, 10)
    print(f"""Vous tombez face à face avec un adversaire de difficulté : {force}
Que voulez-vous faire ?
1- Combattre cet adversaire
2- Contourner cet adversaire et aller ouvrir une autre porte
3- Afficher les règles du jeu
4- Quitter la partie""")

    idiot  =True
    while idiot:
        choice = input()
        if choice in ("1", "2", "3", "4"):
            idiot = False
    if choice == "1":
        combats += 1
        lancers = [rd.randint(1, 6), rd.randint(1, 6)]
        print(f"""Adversaire : {count}
Force de l’adversaire : {force}
Niveau de vie de l’usager : {vies}
Combat {combats} : {victoires} vs {defaites}
Lancer des dé : {lancers[0]}+{lancers[1]}""")

        if lancers[0]+lancers[1] > force:
            print("Dernier combat: Victoire")
            vies += force
            victoires += 1
            consecutives += 1
            print(f"Vicoires consecutives: {consecutives}")
        else:
            print("Dernier combat: Defaite")
            vies -= force
            defaites += 1
            consecutives = 0

        print()

    elif choice == "2":
        vies -= 1
        print(f"Vous perdez un point de vie en trebuchant. Vous etes maintenant a {vies} vies.")

    elif choice == "3":
        print("""Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.
Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.

La partie se termine lorsque les points de vie de l’usager tombent sous 0.

L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
""")
    else:
        print("Merci et au revoir...")
        break
print(f"La partie est terminée, vous avez vaincu {victoires} monstre(s).")