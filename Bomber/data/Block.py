
import pygame as pg
from data.constants import *
import random



class Block(pg.sprite.Sprite):

  def __init__(self,x,y,dx,dy):
    pg.sprite.Sprite.__init__(self)
    self.pos = (x,y)
    self.speed = (dx,dy)
    self.rotation = 0
    self.image = pg.Surface((50, 50))
    self.rockType = (x % 4) #self.rand()
    self.rect = self.image.get_rect()
    self.rect.topright = self.pos
 
  def rand(self):
    # can't use randint in a constructor
    return random.randint(1,4,1)

  def update(self):
    # apply grav
    if self.pos[1] < HEIGHT-self.rect[3]-75:
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
    self.rect.topright = self.pos

    #self.image = rocks[self.rockType]
    self.rotation += 1
    self.image = pg.transform.rotate(rocks[self.rockType],self.rotation)  


    return [0]
  
  def die(self):
    self.kill()
