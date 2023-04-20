import pyxel, random

pyxel.init(128, 128, title="Game_learn")     # Création de la fenêtre de jeu.

vaisseau_x = 60         # Endroit d'apparition de l'objet
vaisseau_y = 60         # Endroit d'apparition de l'objet

vies = 1

tirs_liste = []

ennemis_liste = []

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

# =========================================================
# == TIRS
# =========================================================
def tirs_creation(x, y, tirs_liste):
    """création d'un tir avec la barre d'espace"""

    # btnr pour eviter les tirs multiples
    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs_liste.append([x+4, y-4])
    return tirs_liste

def tirs_deplacement(tirs_liste):
    """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""

    for tir in tirs_liste:
        tir[1] -= 1
        if  tir[1]<-8:
            tirs_liste.remove(tir)
    return tirs_liste

# =========================================================
# == ENNEMIS
# =========================================================

def ennemis_creation(ennemis_liste):
    """création aléatoire des ennemis"""

    # un ennemi par seconde
    if (pyxel.frame_count % 30 == 0):
        ennemis_liste.append([random.randint(0, 120), 0])
    return ennemis_liste


def ennemis_deplacement(ennemis_liste):
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""

    for ennemi in ennemis_liste:
        ennemi[1] += 1
        if  ennemi[1]>128:
            ennemis_liste.remove(ennemi)
    return ennemis_liste

# =========================================================
# == COLLISIONS
# =========================================================

def vaisseau_suppression(vies):
    """disparition du vaisseau et d'un ennemi si contact"""

    for ennemi in ennemis_liste:
        if ennemi[0] <= vaisseau_x+8 and ennemi[1] <= vaisseau_y+8 and ennemi[0]+8 >= vaisseau_x and ennemi[1]+8 >= vaisseau_y:
            ennemis_liste.remove(ennemi)
            vies = 0
    return vies


def ennemis_suppression():
    """disparition d'un ennemi et d'un tir si contact"""

    for ennemi in ennemis_liste:
        for tir in tirs_liste:
            if ennemi[0] <= tir[0]+1 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1]:
                ennemis_liste.remove(ennemi)
                tirs_liste.remove(tir)

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, tirs_liste, ennemis_liste, vies

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = deplacement_vaisseau(vaisseau_x, vaisseau_y)

    # creation des tirs en fonction de la position du vaisseau
    tirs_liste = tirs_creation(vaisseau_x, vaisseau_y, tirs_liste)

    # mise a jour des positions des tirs
    tirs_liste = tirs_deplacement(tirs_liste)

    # creation des ennemis
    ennemis_liste = ennemis_creation(ennemis_liste)

    # mise a jour des positions des ennemis
    ennemis_liste = ennemis_deplacement(ennemis_liste)

        # suppression des ennemis et tirs si contact
    ennemis_suppression()

    # suppression du vaisseau et ennemi si contact
    vies = vaisseau_suppression(vies)

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(6)

    if vies > 0:    

        # vaisseau (carre 8x8)
        pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

        # tirs
        for tir in tirs_liste:
            pyxel.rect(tir[0], tir[1], 1, 4, 10)

        # ennemis
        for ennemi in ennemis_liste:
            pyxel.rect(ennemi[0], ennemi[1], 8, 8, 8)

    # sinon: GAME OVER
    else:

        pyxel.text(50,64, 'GAME OVER', 7)

    

pyxel.run(update, draw)         # appelle aux deux fonction prédéfinies globale et draw. (obligatoire)