import pyxel

pyxel.init(128, 128, title="snake")     # Création de la fenêtre de jeu.

vaisseau_x = 60
vaisseau_y = 60


def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = (vaisseau_x, vaisseau_y)

def draw():

    pyxel.cls(0)

    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

pyxel.run(update, draw)         # appelle aux deux fonction prédéfinies. (obligatoire)