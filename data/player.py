
import pygame as pg
from data.globals import *

class Player(pg.sprite.Sprite):

  def __init__(self,pos,color):
    pg.sprite.Sprite.__init__(self)
    self.color = color
    self.posX = pos[0]
    self.posY = pos[1]
    self.speedX = 0
    self.speedY = 0
    self.shooting = 0
    self.walking = 0
    self.facingR = 1
    self.reload = 100
    self.start_ticks = pg.time.get_ticks()
    self.image = pg.Surface((50, 20))
    self.rect = self.image.get_rect()
    self.rect.center = (self.posX-25,self.posY-10)


  def button(self, input):

    if input == 1:      self.moveX(-1) # l
    if input == 2:      self.moveX(1) # r
    if input == 3:      self.moveY(-1) # u
    if input == 4:      self.moveY(1) # d
    if input == 5:      self.shooting = 1 # print('ranged attack')
    if input == 6:      self.shooting = 1 # print('jump')
    if input == 7:      self.shooting = 1 # print('mellee attack')
    if input == 8:      self.shooting = 1 # print('4th thing')

    if input >= 9:      print('button '+str(input)+' pressed' )

  def moveX(self,input):
      if abs(self.speedX) < MAXSPEED: self.speedX -= input*3

  def moveY(self,input):
      if abs(self.speedY) < MAXSPEED: self.speedY -= input*3
      

  def update(self):

    # apply friction 
    self.speedX = self.speedX*FRICTION
    self.speedY = self.speedY*FRICTION
    
    self.facingR = int(self.speedX+1)

    # stop if slow
    if abs(self.speedX) < .08:
      self.speedX = 0
    if abs(self.speedY) < .08:
      self.speedY = 0
    if abs(self.speedX)+abs(self.speedY) < .16:
      self.walking = 0
    else:
      self.walking = 1

    # apply speed + border checking
    if self.posX < 25:
      self.speedX = 0
      self.posX = 26
    if self.posX > WIDTH-25:
      self.speedX = 0
      self.posX = WIDTH-26
    if self.posY < 10:
      self.speedY = 0
      self.posY = 11
    if self.posY > HEIGHT-100:
      self.speedY = 0
      self.posY = HEIGHT-110
    else:
      self.posX += self.speedX
      self.posY += self.speedY


    # draw new postion
    self.rect.center = (self.posX,self.posY)
    frame = int((pg.time.get_ticks()-self.start_ticks)/100)%9

    if self.walking:
      if self.facingR > 0:
        self.image = ninjagirl_run_anim_R[frame]
      else:
        self.image = ninjagirl_run_anim_L[frame]

    else:
      if self.facingR > 0:
        self.image = ninjagirl_idle_anim_R[frame]
      else:
        self.image = ninjagirl_idle_anim_L[frame]

  
    self.reload += 1

    if self.shooting and self.reload >= 10:
        self.reload = 0
        self.shooting = 0
        return ['Bomb',int(self.posX), int(self.posY),self.speedX,self.speedY]
    self.shooting = 0

    return [0]


  def takeHit(self):
    pass

    
  def die(self):
    print('Im dead')
    return ['GAMEOVER',int(self.posX), int(self.posY),self.speedX,self.speedY]


