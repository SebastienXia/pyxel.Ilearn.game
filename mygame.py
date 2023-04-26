import pyxel

# Initialisation de la fenêtre Pyxel
pyxel.init(120, 160, title="Plateforme")

# Définition des constantes
GRAVITE = 0.2
VITESSE_SAUTE = -5

# Définition des variables
personnage_x = 50
personnage_y = 80
vitesse_y = 0
plateforme_y = 120
sur_plateforme = False

# Fonction de déplacement du personnage
def deplacement_personnage():
    global personnage_x, personnage_y, vitesse_y, sur_plateforme
    
    # Déplacement horizontal du personnage
    if pyxel.btn(pyxel.KEY_RIGHT) and personnage_x < 110:
        personnage_x += 2
    elif pyxel.btn(pyxel.KEY_LEFT) and personnage_x > 0:
        personnage_x -= 2
        
    # Saut du personnage
    if pyxel.btn(pyxel.KEY_SPACE) and sur_plateforme:
        vitesse_y = VITESSE_SAUTE
        sur_plateforme = False
    
    # Gravité
    vitesse_y += GRAVITE
    personnage_y += vitesse_y
    
    # Empêcher le personnage de sortir de l'écran
    if personnage_y > 140:
        personnage_y = 140
        vitesse_y = 0
        
    # Vérifier si le personnage est sur la plateforme
    if personnage_y + 16 >= plateforme_y and personnage_y + 16 <= plateforme_y + 4 and vitesse_y >= 0:
        sur_plateforme = True
        vitesse_y = 0
        personnage_y = plateforme_y - 16
    
# Fonction de mise à jour
def update():
    deplacement_personnage()

# Fonction de dessin
def draw():
    pyxel.cls(0)
    pyxel.rect(0, plateforme_y, 120, 4, 3) # dessiner la plateforme
    pyxel.rect(personnage_x, personnage_y, 16, 16, 9) # dessiner le personnage
    
# Démarrer Pyxel
pyxel.run(update, draw)
