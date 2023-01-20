
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




'''
We were told during the 'get to know the ATO' webinar that
our first rotation placements were being worked out at the time.
If these placements are decided can/will we be told prior to comencment?
I would very much like to research/revise the subject at least a little this month.
'''