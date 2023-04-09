import pyxel

pyxel.init(128, 128, title="Game_learn")     # Création de la fenêtre de jeu.

vaisseau_x = 60         # Endroit de d'apparition de l'objet
vaisseau_y = 60         # Endroit de d'apparition de l'objet

def deplacement_vaisseau(x, y):

# Touche de déplacement de l'objet | Z D S Q

    if pyxel.btn(pyxel.KEY_D):
        if x < 120:
            x = x + 1
    if pyxel.btn(pyxel.KEY_Q):
        if x > 0:
            x = x - 1
    if pyxel.btn(pyxel.KEY_S):
        if y < 120:
            y = y + 1
    if pyxel.btn(pyxel.KEY_Z):
        if y > 0:
            y = y - 1

    return x, y


def update():

# update des variable à chauqe fois.

    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y       # fonction global (obligatoire)

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = deplacement_vaisseau (vaisseau_x, vaisseau_y)      # Faire en sorte que l'objet bouge grâce aux touches

def draw():

# Dessine le code.

    pyxel.cls(5)

    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

pyxel.run(update, draw)         # appelle aux deux fonction prédéfinies globale et draw. (obligatoire)