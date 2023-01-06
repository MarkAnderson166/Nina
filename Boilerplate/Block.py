
import pygame as pg
from constants import *


class Block(pg.sprite.Sprite):

  def __init__(self,x,y,dx,dy):
    pg.sprite.Sprite.__init__(self)
    self.color = ((50,50,200))
    self.pos = (x,y)
    self.speed = (dx,dy)
    self.image = pg.Surface((20, 20))
    self.rect = self.image.get_rect()
    self.rect.center = self.pos
 
  def update(self):
    # apply grav
    if self.pos[1] < HEIGHT-self.rect[3]:
      self.speed = (self.speed[0],self.speed[1]+GRAVITY)
    else:
      # if you stop moving, you'll die
      if abs(self.speed[1]) < GRAVITY/2:
        self.die()
      # bounce
      self.speed = (self.speed[0],self.speed[1]*-.9)
    # bounce off walls
    if self.pos[0] < 0+self.rect[3] or self.pos[0] > WIDTH-self.rect[3]:
      self.speed = (self.speed[0]*-.9,self.speed[1])
    # apply speed change
    self.pos = (self.pos[0]+self.speed[0],self.pos[1]+self.speed[1])
  # draw new postion
    self.rect.center = self.pos
    self.image.fill(self.color)

    return [0]
  
  def die(self):
    self.kill()
