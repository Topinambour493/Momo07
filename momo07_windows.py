def waitclic():
    """ attend que l'utilisateur clique droit, et renvoie les coordonnées du point cliqué. ferme le programme si clic sur croix"""
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type== MOUSEBUTTONDOWN :
                return event.pos

def signe_momo():
    if balles_momo.nb()==0 and balles_joueur.nb()==0:
        return "recharge"
    if balles_momo.nb()>=1:
        return signes[random.randint(0,2)]
    return signes[random.randint(0,1)]

def signe_joueur():
    joueur=0
    while joueur==0:
        x,y=waitclic()
        if 660<=y<=760:
            if coordonées_recharge[0]<=x<=coordonées_recharge[0]+100:
                joueur="recharge"
            elif coordonées_tir[0]<=x<=coordonées_tir[0]+100 and balles_joueur.nb()>=1:
                joueur="tir"
            elif coordonées_bouclier[0]<=x<=coordonées_bouclier[0]+100:
                joueur="bouclier"
    return joueur

#définition de la fonction carré plein
def carre_plein(centre,t,couleur):
    while t>-1:
        x1,y1=(centre[0]+t,centre[1]-t)
        x2,y2=(centre[0]+t,centre[1]+t)
        x3,y3=(centre[0]-t,centre[1]+t)
        x4,y4=(centre[0]-t,centre[1]-t)
        pygame.draw.line(screen,couleur,(x1,y1),(x2,y2),1)
        pygame.draw.line(screen,couleur,(x2,y2),(x3,y3),1)
        pygame.draw.line(screen,couleur,(x3,y3),(x4,y4),1)
        pygame.draw.line(screen,couleur,(x4,y4),(x1,y1),1)
        t=t-1

def actions(signe_j,signe_m):
    print(signe_j,signe_m)
    if signe_j=="recharge":
        balles_joueur.recharge()
        window.blit(joueur_recharge,(150,472))
        if signe_m=="recharge":
            balles_momo.recharge()
            window.blit(momo_recharge,(0,0))
        elif signe_m=="tir":
            balles_momo.tir()
            window.blit(momo_tir,(0,0))
            return "momo"
        else:
            window.blit(momo_bouclier,(0,0))
    elif signe_j=="tir":
        balles_joueur.tir()
        window.blit(joueur_tir,(150,472))
        if signe_m=="recharge":
            balles_momo.recharge()
            window.blit(momo_recharge,(0,0))
            return "joueur"
        elif signe_m=="tir":
            balles_momo.tir()
            window.blit(momo_tir,(0,0))
            return 1
        else:
            window.blit(momo_bouclier,(0,0))
    else:
        window.blit(joueur_bouclier,(150,472))
        if signe_m=="recharge":
            balles_momo.recharge()
            window.blit(momo_recharge,(0,0))
        elif signe_m=="tir":
            balles_momo.tir()
            window.blit(momo_tir,(0,0))
        else:
            window.blit(momo_bouclier,(0,0))
    return 0

def affiche_actions_possibles():
    window.blit(joueur_recharge,coordonées_recharge)
    if balles_joueur.nb()==0:
        window.blit(joueur_tir_impossible,coordonées_tir)
    else:
        window.blit(joueur_tir,coordonées_tir)
    window.blit(joueur_bouclier,coordonées_bouclier)
    pygame.display.flip()

#définition de la fonction affichage_texte
def affichage_texte(texte,color,pos):
    text=font.render(texte,1,color)
    window.blit(text,pos)

class Balles:
    def __init__(self):
        self.NbBalles=0

    def nb(self):
        return self.NbBalles

    def recharge(self):
        self.NbBalles+=1

    def tir(self):
        self.NbBalles-=1

    def reinitialise(self):
        self.NbBalles=0

#INITIALISATION
import pygame
import random
from pygame.locals import *
pygame.init() # initialisation de pygame
#construit la fenetre
window= pygame.display.set_mode((400,770))
screen = pygame.display.get_surface()

#chargement des images
momo_tir = pygame.image.load("images/momo/pistolet.png").convert_alpha()
balles = pygame.image.load("images/général/nb_balles.png").convert_alpha()
momo_recharge =  pygame.image.load("images/momo/recharge.jpg").convert_alpha()
momo_bouclier = pygame.image.load("images/momo/bouclier.jpg").convert_alpha()
momo_bonjour = pygame.image.load("images/momo/bonjour.jpg").convert_alpha()
momo_ntm = pygame.image.load("images/momo/ntm.jpg").convert_alpha()
joueur_recharge = pygame.image.load("images/joueur/recharger.png").convert_alpha()
joueur_tir = pygame.image.load("images/joueur/pistolet.png").convert_alpha()
joueur_tir_impossible = pygame.image.load("images/joueur/pistolet_impossible.png").convert()
joueur_bouclier = pygame.image.load("images/joueur/bouclier.png").convert_alpha()

#chargement de la font
font=pygame.font.SysFont("Calibri",32,bold=False,italic=False)

#variables jeu
blanc=(255,255,255)
noir=(0,0,0)
coordonées_recharge=(40,660)
coordonées_tir=(150,660)
coordonées_bouclier=(260,660)
pts_joueur=0
pts_momo=0
balles_momo=Balles()
balles_joueur=Balles()
signes=["bouclier","recharge","tir"]
window.blit(momo_bonjour,(0,0))
while 3 not in [pts_joueur,pts_momo]:
    balles_momo.reinitialise()
    balles_joueur.reinitialise()
    vainqueur_manche=0
    while (vainqueur_manche==0):
        window.blit(balles,(0,0))
        window.blit(balles,(0,462))
        affichage_texte(str(balles_momo.nb()),blanc,(50,4))
        affichage_texte(str(balles_joueur.nb()),blanc,(50,466))
        affichage_texte(str(pts_momo),blanc,(370,4))
        carre_plein((380,486),20,noir)
        affichage_texte(str(pts_joueur),blanc,(370,466))
        affiche_actions_possibles()
        vainqueur_manche=actions(signe_joueur(),signe_momo())
        pygame.display.flip()
    if vainqueur_manche=="momo":
        pts_momo+=1
    elif vainqueur_manche=="joueur":
        pts_joueur+=1
    print(pts_momo,pts_joueur)
    window.blit(balles,(0,0))
    window.blit(balles,(0,462))
window.fill(noir)
window.blit(momo_ntm,(0,0))
affichage_texte(str(pts_momo),blanc,(370,4))
carre_plein((380,486),20,noir)
affichage_texte(str(pts_joueur),blanc,(370,466))
if pts_joueur>pts_momo:
    affichage_texte("GAGNÉ!",blanc,(150,600))
else:
    affichage_texte("PERDU!",blanc,(150,600))
pygame.display.flip()
while True:
    waitclic()













