print("Afficher du texte : print()")

# Mon tout premier programme Python pour l'IA !
# Le # introduit un commentaire : Python l'ignore complètement.
# Les commentaires servent à expliquer le code — prends l'habitude d'en écrire !

print("boujour")
print("halooooo")


print("Les variables et les types")

prenom = "Alice"       # str   : chaîne de caractères (entre guillemets)
age    = 20            # int   : nombre entier
note   = 15.5          # float : nombre décimal (avec un point, pas une virgule !)
admis  = True          # bool  : vrai (True) ou faux (False)

print(prenom, "a", age, "ans — note :", note, "— admis :", admis)


print("Les listes")

notes = [14, 18, 12, 16, 9]    # liste de 5 entiers

print(notes)           # affiche [14, 18, 12, 16, 9]
print(notes[0])        # affiche 14  (le 1er élément — indice 0)
print(notes[4])        # affiche 9   (le 5e élément — indice 4)
print(len(notes))      # affiche 5   (nombre d'éléments dans la liste)


print("La boucle for")

note = 14

notes = [14, 18, 12, 16, 9]

for n in notes:
    print("Note :", n)    # <-- ce bloc est décalé de 4 espaces : c'est l'indentation


print("L'instruction if ... else")

note = 14

if note >= 10:
    print("Admis")      # <-- bloc exécuté si la condition est vraie
else:
    print("Ajourné")    # <-- bloc exécuté si la condition est fausse

