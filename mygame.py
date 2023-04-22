import pyxel, time, random


pyxel.init(128, 128, title="Game_learn")

personnage_position_x = 3
personnage_position_y = 117

dernier_saut = 0

coup_épée = []
dernier_coup = 0

goblins = []

animation_frames = [0, 1]
frame_counter = 0

pyxel.load("my_game_ressources.pyxres")

vitesse_y = 0

def deplacement_personnage(x, y):

    global vitesse_y, dernier_saut

    temps_actuel = time.time()

    if pyxel.btn(pyxel.KEY_D):
        if x < 118:
            x += 1
    if pyxel.btn(pyxel.KEY_Q):
        if x > 2:
            x -= 1
    if pyxel.btn(pyxel.KEY_S):
        if y < 117:
            y += 1

    # Ajouter la gravité
    vitesse_y += 0.5  # ajuster la valeur de gravité selon vos besoins
    y += int(vitesse_y)  # convertir la vitesse en entier pour éviter des pixels partiels

    # Empêcher le personnage de sortir de l'écran en bas
    if y > 117:
        y = 117
        vitesse_y = 0

    # Sauter lorsque la touche Z est pressée
    if pyxel.btn(pyxel.KEY_Z) and temps_actuel - dernier_saut >= 1:
        vitesse_y = -5  # ajuster la valeur selon vos besoins
        dernier_saut = temps_actuel

    return x, y


def coup_création(x, y, coup_épée):
    global dernier_coup

    temps_actuel = time.time()

    if pyxel.btnr(pyxel.KEY_SPACE) and temps_actuel - dernier_coup >= 1: # vérification de la touche et de la pause de 2 secondes
        coup_épée.append([x+8, y])
        dernier_coup = temps_actuel  # mise à jour du temps de la dernière création de coup
        
    return coup_épée

def coup_deplacement(coup_épée):
    for coups in coup_épée:
        coups[0] += 1  # ajouter 1 à la coordonnée x de chaque coup pour que le coup aille vers la droite
        if coups[1] > 128:
            coup_épée.remove(coups)
            

    return coup_épée

# =========================================================
# == GOBLINS
# =========================================================

def ennemis_creation(goblins):
    """création aléatoire des ennemis"""

    # un ennemi par seconde
    if (pyxel.frame_count % 70 == 0):
        goblins.append([random.randint(117, 130), 117,])
    return goblins

def ennemis_deplacement(ennemis_liste):
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""

    for ennemi in goblins:
        ennemi[0] -= 1
        if  ennemi[1]>128:
            goblins.remove(ennemi)
    return goblins

# =========================================================
# == UPDATE
# =========================================================

def update():

    global personnage_position_x, personnage_position_y, coup_épée, goblins, frame_counter

    frame_counter += 1
    if frame_counter >= len(animation_frames):
        frame_counter = 0

    personnage_position_x, personnage_position_y = deplacement_personnage(personnage_position_x, personnage_position_y)

    coup_épée = coup_création(personnage_position_x, personnage_position_y, coup_épée)

    coup_épée = coup_deplacement(coup_épée)

    goblins = ennemis_creation(goblins)

    goblins = ennemis_deplacement(goblins)

    if pyxel.btnp(pyxel.KEY_ESCAPE):
        pyxel.quit()

# =========================================================
# == DRAW
# =========================================================
def draw():

    pyxel.cls(0)

    pyxel.bltm(50, 60, 0, 0, 0, 128, 128, 0)

    pyxel.blt(3, 117, 0, 40, 0, 8, 8, 0)

    for torches in range(5):
        pyxel.blt(20 + (torches * 20), 115, 0, 40, 8, 8, 8, 0)

    pyxel.blt(personnage_position_x, personnage_position_y, 0, 16, 0, 8, 8, 0)

    if pyxel.btn(pyxel.KEY_D):
        pyxel.blt(personnage_position_x, personnage_position_y, 0, animation_frames[frame_counter] * 8, 0, 8, 8, 1)

    if pyxel.btn(pyxel.KEY_Q):
        pyxel.blt(personnage_position_x, personnage_position_y, 0,animation_frames[frame_counter] * 8, 8, 8, 8, 1)

    if pyxel.btnr(pyxel.KEY_SPACE):
        pyxel.blt(personnage_position_x, personnage_position_y, 0, 0, 16, 8, 8, 0)

    for coups in coup_épée:
        pyxel.blt(coups[0], coups[1], 0, 8, 16, 8, 8, 0)

    for sols in range(16):
        pyxel.blt(0 + (sols * 8), 125, 0, 48, 8, 10, 50, 0)

    for ennemi in goblins:
        pyxel.blt(ennemi[0], ennemi[1], 0, animation_frames[frame_counter] * 8, 24, 8, 8, 0)

pyxel.run(update, draw)

# pyxel edit my_game_ressources