import pyxel, time

pyxel.init(160, 120)

# DEPLACEMENT DU PERSONNAGE

personnage_x = 5
personnage_y = 107

vitesse_y = 0
dernier_saut = 0

def deplacement_personnage(x, y):

    global vitesse_y, dernier_saut
    temps_actuel = time.time()

    if pyxel.btn(pyxel.KEY_D):
        if x < 160:
            x += 1
    if pyxel.btn(pyxel.KEY_Q):
        if x > 0:
            x -= 1
    if pyxel.btn(pyxel.KEY_S):
        if y < 105:
            y += 1

    # ajout de la gravité avec la variable "vitesse_y"
    vitesse_y += 0.5
    y += int(vitesse_y)

    # Eviter que le personnage sorte de l'écran en bas
    if y > 105:
        y = 105
        vitesse_y = 0

    #Saut lorsque le bouton Z est touché
    if pyxel.btn(pyxel.KEY_Z) and temps_actuel - dernier_saut >= 1: # Tous les 2 secondes
        vitesse_y = -5
        dernier_saut = temps_actuel

    return x, y

# ATTACK DU PERSONNAGE

coup_epee_droite = []
dernier_coup_droite = 0

def coup_creation_droite(x, y, coup_epee_droite):
    global dernier_coup_droite

    temps_actuel = time.time()

    if pyxel.btnr(pyxel.KEY_E) and temps_actuel - dernier_coup_droite >= 1:
        coup_epee_droite.append([x+9, y+4])
        dernier_coup_droite = temps_actuel
    return coup_epee_droite

def coup_deplacement_droite(coup_epee_droite):
    for coups in coup_epee_droite:
        coups[0] += 1
        if coups[1] < -8:
            coup_epee_droite.remove(coups)
    return coup_epee_droite

dernier_coup = 0
coup_epee_gauche = []

def coup_creation_gauche(x, y, coup_epee_gauche):
    global dernier_coup
    
    temps_actuel = time.time()
    
    if pyxel.btnr(pyxel.KEY_A) and temps_actuel - dernier_coup >= 1:
        coup_epee_gauche.append([x-9, y+4])
        dernier_coup = temps_actuel
    
    return coup_epee_gauche

def coup_deplacement_gauche(coup_epee_gauche):
    for coups in coup_epee_gauche:
        coups[0] -= 1
        if coups[1] < -8:
            coup_epee_gauche.remove(coups)
    return coup_epee_gauche

# =========================================================
# == UPDATE
# =========================================================
def update():

    global personnage_x, personnage_y, coup_epee_droite, coup_epee_gauche

    if pyxel.btnp(pyxel.KEY_ESCAPE):
        pyxel.quit()

    personnage_x, personnage_y = deplacement_personnage(personnage_x, personnage_y)

    coup_epee_droite = coup_creation_droite(personnage_x, personnage_y, coup_epee_droite)

    coup_epee_droite = coup_deplacement_droite(coup_epee_droite)

    coup_epee_gauche = coup_creation_gauche(personnage_x, personnage_y, coup_epee_gauche)

    coup_epee_gauche = coup_deplacement_gauche(coup_epee_gauche)


# =========================================================
# == DRAW
# =========================================================
def draw():
    pyxel.cls(0)

    pyxel.rect(personnage_x, personnage_y, 8, 8, 1)

    for coups in coup_epee_droite:
        pyxel.rect(coups[0], coups[1], 4, 1, 5)

    for coups in coup_epee_gauche:
        pyxel.rect(coups[0], coups[1], 4, 1, 5)

pyxel.run(update, draw)