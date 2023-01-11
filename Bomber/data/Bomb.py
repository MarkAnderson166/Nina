
import pygame as pg
from data.constants import *

class Bomb(pg.sprite.Sprite):

  def __init__(self,x,y,dx,dy):
    pg.sprite.Sprite.__init__(self)
    self.pos = (x,y)
    self.speed = (dx,dy)
    self.dieing = 0
    self.image = pg.Surface((15, 15))
    self.rect = self.image.get_rect()
    self.rect.topleft = self.pos
 
  def update(self):

    # apply grav
    if self.pos[1] < HEIGHT-self.rect[3]-75:
      self.speed = (self.speed[0],self.speed[1]+GRAVITY)
    else:
      # explode of ground
      self.die()

    # bounce off walls
    if self.pos[0] < 0+self.rect[3] or self.pos[0] > WIDTH-self.rect[3]:
      self.speed = (self.speed[0]*-.7,self.speed[1])

    # apply speed change
    self.pos = (self.pos[0]+self.speed[0],self.pos[1]+self.speed[1])
  
    # draw new postion
    self.rect.topleft = self.pos
    self.image = bombimage

    if self.dieing == 1:
      #print('making a fire at: '+str(int(self.pos[0]))+', '+str(self.pos[1]))
      self.kill()
      return ['Fire',int(self.pos[0]), int(self.pos[1]),0,self.speed[1]]
    return [0]
  
  def die(self):
    self.dieing = 1
    
