
import pygame as pg
from constants import *

class Fire(pg.sprite.Sprite):

  def __init__(self,x,y,dx,dy):
    pg.sprite.Sprite.__init__(self)
    self.color = 50
    self.pos = (x,y-30)
    self.speed = (dx,dy)
    self.size = 60
    self.image = pg.Surface((self.size, self.size))
    self.rect = self.image.get_rect()
    self.rect.center = self.pos
 
  def update(self):

    # fall in air, burn on ground
    if self.pos[1] > HEIGHT-self.size:
      self.speed = (0,0)

    # die slowly
    self.size -= 1
    self.pos = (self.pos[0]+.5,self.pos[1]+.5)
    if self.size < 5:
      self.die()

    # apply speed change
    self.pos = (self.pos[0]+self.speed[0],self.pos[1]+self.speed[1])

    # draw new postion
    self.rect.center = self.pos
    self.color += 10
    if self.color > 240: self.color = 0
    self.image = pg.Surface((self.size, self.size))
    self.image.fill((255,self.color,0))

    return [0]
  
  def die(self):
    self.kill()
    




