
import pygame as pg
from data.toon import *
from data.globals import *

class Enemy(Toon):
  def __init_(self,pos,type):
    super().__init__(pos,type)
    self.dummy = 0
  
  def button(self, input):

    if input == 1:      self.moveX(-1) # l
    if input == 2:      self.moveX(1) # r
    if input == 3:      self.moveY(-1) # u
    if input == 4:      self.moveY(1) # d
    if input == 5:      self.isShooting = 1
    if input == 6:
      self.isDying = 1
      self.start_ticks = pg.time.get_ticks()
    if input == 7:
      self.isDead = 0 
    if input == 8:
      self.isAttacking = 1
      self.start_ticks = pg.time.get_ticks()
    if input >= 9:      print('button '+str(input)+' pressed' )
    


