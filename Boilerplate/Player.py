
import pygame as pg
from constants import *

class Player(pg.sprite.Sprite):

  def __init__(self,pos,color):
    pg.sprite.Sprite.__init__(self)
    self.color = color
    self.posX = pos[0]
    self.posY = pos[1]
    self.speedX = 0
    self.speedY = 0
    self.shooting = 0
    self.health = 150
    self.image = pg.Surface((self.health/2, self.health/3))
    self.rect = self.image.get_rect()
    self.rect.center = (self.posX,self.posY)


  def button(self, input):
    if input == 0:      self.shooting = 1 # print('mellee attack')
    if input == 1:      self.shooting = 1 # print('ranged attack')
    if input == 2:      self.shooting = 1 # print('jump')
    if input == 3:      self.shooting = 1 # print('4th thing')
    if input >= 4:      print('button '+str(input)+' pressed' )

  def moveX(self,input):
      if abs(self.speedX) < MAXSPEED: self.speedX -= input

  def moveY(self,input):
      if abs(self.speedY) < MAXSPEED: self.speedY -= input
      

  def update(self):

    if self.health < 30:
      self.die()

    # apply friction 
    self.speedX = self.speedX*FRICTION
    self.speedY = self.speedY*FRICTION

    # stop if slow
    if abs(self.speedX) < .08: self.speedX = 0
    if abs(self.speedY) < .08: self.speedY = 0

    # apply speed 
    self.posX += self.speedX
    self.posY += self.speedY 

    # draw new postion
    self.rect.center = (self.posX,self.posY)
    self.image = pg.Surface((self.health/2, self.health/3))
    self.image.fill(self.color)
  
    if self.shooting:
      self.shooting = 0
      return ['Bomb',int(self.posX), int(self.posY)+30,self.speedX,self.speedY]
    return [0]

  def takeHit(self):
    self.health -= 10
    print('I got hit')
    
  def die(self):
    print('Im dead')
    self.kill()



