import math  # Importation du module math pour utiliser la fonction sqrt (racine carrée)

def calc_distance(point1, point2):
    # Vérification que chaque point contient bien deux coordonnées
    if len(point1) != 2 or len(point2) != 2:
        raise ValueError("Chaque point doit avoir exactement deux coordonnées (x et y)")

    # Calcul de la différence entre les coordonnées x des deux points
    dx = point2[0] - point1[0]

    # Calcul de la différence entre les coordonnées y des deux points
    dy = point2[1] - point1[1]

    # Calcul de la distance euclidienne à partir des différences
    distance = math.sqrt(dx**2 + dy**2)  # La formule d = sqrt(dx^2 + dy^2)

    return distance  # Retourne la distance calculée

# Exemple d'utilisation
# Définir deux points avec des coordonnées x et y
point1 = [1, 2]
point2 = [4, 6]

# Appeler la fonction pour obtenir la distance entre ces deux points
distance = calc_distance(point1, point2)

print(f"La distance entre les points {point1} et {point2} est de {distance} unités.")
