
import pygame as pg
import os

HEIGHT = 900
WIDTH = 1600
FPS = 60

GRAVITY = .2
MAXSPEED = 40
FRICTION = .7

game_folder = os.path.dirname(__file__)

background_folder = os.path.join(game_folder, "background")
backgroundimage = pg.image.load(os.path.join(background_folder, "game_background_1.png"))
backgroundimage = pg.transform.scale(backgroundimage, (WIDTH, HEIGHT))

img_folder = os.path.join(game_folder, "toon")
img_folder = os.path.join(img_folder, "ninjagirl")

ninjagirl_idle_anim_R = []
ninjagirl_idle_anim_L = []

for i in range(0,9,1):
  filename = "Idle__00{}.png".format(i)
  img = pg.image.load(os.path.join(img_folder, filename))
  img = pg.transform.scale(img, (145,250))
  ninjagirl_idle_anim_R.append(img)
  img = pg.transform.flip(img, 1,0)
  ninjagirl_idle_anim_L.append(img)


ninjagirl_run_anim_R = []
ninjagirl_run_anim_L = []
for i in range(0,9,1):
  filename = "Run__00{}.png".format(i)
  img = pg.image.load(os.path.join(img_folder, filename))
  img = pg.transform.scale(img, (175,250))
  ninjagirl_run_anim_R.append(img)
  img = pg.transform.flip(img, 1,0)
  ninjagirl_run_anim_L.append(img)

