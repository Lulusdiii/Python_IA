print("Les fonctions avec def")

# Définition d'une fonction qui additionne deux nombres
def addition(a, b):
    resultat = a + b
    return resultat

# Appel de la fonction
print(addition(3, 5))      # affiche 8


print("Le module numpy : calculer vite sur des tableaux")

import numpy as np      # convention : on l'abrège en "np"

entrees = np.array([2.0, 3.0])     # un tableau de 2 nombres
poids   = np.array([0.5, -1.0])    # les poids associés

# np.dot fait la somme pondérée d'un coup : (2*0.5) + (3*-1.0)
z = np.dot(entrees, poids)
print(z)        # affiche -2.0


print("Codons notre premier neurone !")

import numpy as np

# --- Le neurone : une fonction qui décide 0 ou 1 ---
def perceptron(entrees, poids, biais):
    z = np.dot(entrees, poids) + biais    # étape 1 : somme pondérée
    if z >= 0:                             # étape 2 : fonction seuil
        return 1                           # étape 3 : décision "activé"
    else:
        return 0                           #            décision "éteint"

# --- On teste notre neurone ---
poids = np.array([0.5, 0.5])    # deux entrées, poids égaux
biais = -0.7

print(perceptron(np.array([1, 1]), poids, biais))   # 1+1 pondéré = 1.0 - 0.7 = 0.3 >= 0 -> 1
print(perceptron(np.array([0, 0]), poids, biais))   # 0 - 0.7 = -0.7 < 0 -> 0


print("Visualiser la frontière de décision sur de vraies fleurs")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron

# 1. Charger les données, garder 2 classes et 2 caractéristiques
iris = load_iris()
X = iris.data[:100, 2:4]      # 100 premières fleurs, colonnes pétale (longueur, largeur)
y = iris.target[:100]         # étiquettes : 0 = setosa, 1 = versicolor

# 2. Créer et entraîner le perceptron
modele = Perceptron()
modele.fit(X, y)              # le neurone ajuste tout seul ses poids et son biais

# 3. Afficher les fleurs colorées par espèce
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="bwr", edgecolor="k")
plt.xlabel("Longueur du pétale (cm)")
plt.ylabel("Largeur du pétale (cm)")
plt.title("Perceptron : la frontière qui sépare 2 espèces de fleurs")

# 4. Tracer la frontière de décision (la droite trouvée par le neurone)
w = modele.coef_[0]           # les poids appris
b = modele.intercept_[0]      # le biais appris
x_vals = np.array([X[:, 0].min(), X[:, 0].max()])
y_vals = -(w[0] * x_vals + b) / w[1]
plt.plot(x_vals, y_vals, "k--", linewidth=2)

plt.show()