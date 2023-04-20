import pyxel, time


pyxel.init(128, 128, title="Game_learn")

personnage_position_x = 3
personnage_position_y = 117

sol_x = 0
sol_y = 125

coup_épée = []
dernier_coup = 0

pyxel.load("my_game_ressources.pyxres")

def deplacement_personnage(x, y):
    if pyxel.btn(pyxel.KEY_D):
        if x < 118:
            x +=1
    if pyxel.btn(pyxel.KEY_Q):
        if x > 2:
            x -=1
    if pyxel.btn(pyxel.KEY_S):
        if y < 117:
            y +=1
    if pyxel.btnr(pyxel.KEY_Z):
        if y > 0:
            y -= 5
        
    return(x, y)


def coup_création(x, y, coup_épée):
    
    global dernier_coup

    temps_actuel = time.time()

    if pyxel.btnr(pyxel.KEY_SPACE) and temps_actuel - dernier_coup >= 1:  # vérification de la touche et de la pause de 2 secondes
        coup_épée.append([x+8, y])
        dernier_coup = temps_actuel  # mise à jour du temps de la dernière création de coup

    return coup_épée

def coup_deplacement(coup_épée):
    for coups in coup_épée:
        coups[0] +=1  # ajouter 1 à la coordonnée x de chaque coup pour que le coup aille vers la droite
        if coups[1] > 128:
            coup_épée.remove(coups)

    return coup_épée


# =========================================================
# == UPDATE
# =========================================================

def update():

    global personnage_position_x, personnage_position_y, coup_épée

    personnage_position_x, personnage_position_y = deplacement_personnage(personnage_position_x, personnage_position_y)

    coup_épée = coup_création(personnage_position_x, personnage_position_y, coup_épée)

    coup_épée = coup_deplacement(coup_épée)

    if pyxel.btnp(pyxel.KEY_ESCAPE):
        pyxel.quit()

# =========================================================
# == DRAW
# =========================================================
def draw():

    pyxel.cls(0)

    pyxel.blt(personnage_position_x, personnage_position_y, 0, 0, 0, 8, 8, 1)

    if pyxel.btn(pyxel.KEY_Q):
        pyxel.blt(personnage_position_x, personnage_position_y, 0, 0, 8, 8, 8, 1)

    if pyxel.btnr(pyxel.KEY_SPACE):
        pyxel.blt(personnage_position_x, personnage_position_y, 0, 0, 16, 8, 8, 1)

    for coups in coup_épée:
        pyxel.blt(coups[0], coups[1], 0, 8, 8, 8, 8, 10)

    for i in range(16):
        pyxel.blt(0 + (i * 8), 125, 0, 8, 0, 125, 3, 0)

pyxel.run(update, draw)

# pyxel edit my_game_ressources