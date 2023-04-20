import pyxel, random

pyxel.init(128, 128, title="Game_learn")     # Création de la fenêtre de jeu.

vaisseau_x = 60         # Endroit d'apparition de l'objet
vaisseau_y = 60         # Endroit d'apparition de l'objet

vies = 3

tirs_liste = []

ennemis_liste = []

explosions_liste = []

pyxel.load('ressources.pyxres')

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
        tirs_liste.append([x+1, y-7])
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
            vies -= 1
            # on ajoute l'explosion
            explosions_creation(vaisseau_x, vaisseau_y)
    return vies


def explosions_creation(x, y):
    """explosions aux points de collision entre deux objets"""
    explosions_liste.append([x, y, 0])


def ennemis_suppression():
    """disparition d'un ennemi et d'un tir si contact"""

    for ennemi in ennemis_liste:
        for tir in tirs_liste:
            if ennemi[0] <= tir[0]+8 and ennemi[0]+8 >= tir[0] and ennemi[1]+8 >= tir[1]:
                ennemis_liste.remove(ennemi)
                tirs_liste.remove(tir)
                # on ajoute l'explosion
                explosions_creation(ennemi[0], ennemi[1])

def explosions_animation():
    """animation des explosions"""
    for explosion in explosions_liste:
        explosion[2] +=1
        if explosion[2] == 12:
            explosions_liste.remove(explosion) 

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, tirs_liste, ennemis_liste, vies, explosions_liste

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

    # evolution de l'animation des explosions
    explosions_animation()    

# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(6)

    if vies > 0:    

        pyxel.text(5,5,"Vie restant:" + str(vies), 7) 
        # vaisseau (carre 8x8)
        
        pyxel.blt(vaisseau_x, vaisseau_y, 0, 8, 0, 8, 8, 1)

        # tirs
        for tir in tirs_liste:
            pyxel.blt(tir[0], tir[1],0, 8, 8, 8, 8, 10)

        # ennemis
        for ennemi in ennemis_liste:
            pyxel.blt(ennemi[0], ennemi[1],0, 0, 8, 8, 8, 8)
        
                # explosions (cercles de plus en plus grands)
        for explosion in explosions_liste:
            pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3)    

    # sinon: GAME OVER
    else:

        pyxel.text(50,64, 'GAME OVER', 7)

    

pyxel.run(update, draw)         # appelle aux deux fonction prédéfinies globale et draw. (obligatoire)