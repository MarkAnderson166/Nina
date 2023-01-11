
import pygame as pg
from random import randint
import os



HEIGHT = 800
WIDTH = 1400
FPS = 60

GRAVITY = .2
MAXSPEED = 30
FRICTION = .9



game_folder = os.path.dirname(__file__)

img_folder = os.path.join(game_folder, "Background")
backgroundimage = []
for i in range(0,4,1):
  filename = "front_decor{}.png".format(i)
  img = pg.image.load(os.path.join(img_folder, filename))
  img = pg.transform.scale(img, (1400, 800))
  backgroundimage.append(img)

playerimage = pg.image.load(os.path.join(game_folder,'player.png'))
playerimage = pg.transform.scale(playerimage, (100, 40))
img_folder = os.path.join(game_folder, "Fire")

explosion_anim = []
for i in range(0,7,1):
  filename = "00{}.png".format(i)
  img = pg.image.load(os.path.join(img_folder, filename))
  img.set_colorkey((0,0,0))
  img = pg.transform.scale(img, (100,100))
  explosion_anim.append(img)

bombimage = pg.transform.scale(explosion_anim[0], (30, 30))


img_folder = os.path.join(game_folder, "Rocks")
rocks = []
for i in range(1,5,1):
  filename = "rock{}.png".format(i)
  img = pg.image.load(os.path.join(img_folder, filename))
  img = pg.transform.scale(img, (50,50))
  rocks.append(img)


firePath = os.path.join(os.path.dirname(__file__), "Fire")
boomSound = os.path.join(firePath, 'boom.mp3')
biggerBoomSound = os.path.join(firePath, 'biggerBoom.mp3')


#cMajor = [261,293,329,349,392,440,493,523,587,659,698,784,880,987,1046]
