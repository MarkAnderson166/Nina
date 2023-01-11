
import pygame as pg
from data.constants import *


class Fire(pg.sprite.Sprite):

  def __init__(self,x,y,dx,dy):
    pg.sprite.Sprite.__init__(self)
    self.pos = (x,y-30)
    self.speed = (dx,dy)
    self.frame = 1
    self.image = pg.Surface((50, 50))
    self.rect = self.image.get_rect()
    self.rect.center = self.pos
    try:
      pg.mixer.Sound(boomSound).play(0).set_volume(0.2)
    except:
      print('fire died before sound played')
    #pg.mixer.Sound(biggerBoomSound).play(0)
 
  def update(self):

    # fall in air, burn on ground
    if self.pos[1] > HEIGHT-50:
      self.speed = (0,0)

    # die slowly
    self.pos = (self.pos[0]+.5,self.pos[1]+.5)
    if self.frame > 7:
      self.die()

    # apply speed change
    self.pos = (self.pos[0]+self.speed[0],self.pos[1]+self.speed[1])

    # draw new postion
    self.rect.center = self.pos
    self.image = explosion_anim[self.frame%6+1]
    self.frame += 1

    return [0]
  
  def die(self):
    self.kill()
    

