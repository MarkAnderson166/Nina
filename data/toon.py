
import pygame as pg
from data.globals import *

class Toon(pg.sprite.Sprite):

  def __init__(self,pos,type):
    pg.sprite.Sprite.__init__(self)
    self.type = type
    self.posX = pos[0]
    self.posY = pos[1]
    self.speedX = 0
    self.speedY = 0

    self.isShooting = 0
    self.isDying = 0
    self.isDead = 0
    self.isAttacking = 0
    self.isWalking = 0
    self.facingR = 1

    self.subClassAnimation = 0

    self.start_ticks = pg.time.get_ticks()
    self.image = pg.Surface((1,1))
    self.rect = (self.posX,self.posY,self.image.get_width(),self.image.get_height())
    #self.rect.midbottom = (self.posX,self.posY)

    self.idle_anim_R = []
    self.idle_anim_L = []
    self.run_anim_R = []
    self.run_anim_L = []
    self.dead_anim_R = []
    self.dead_anim_L = []
    self.attack_anim_R = []
    self.attack_anim_L = []
    self.loadAssets()

  def getRect(self):
    return self.rect

  def loadAssets(self):

    img_folder = os.path.join(game_folder, "toon")
    img_folder = os.path.join(img_folder, self.type)

    for i in range(9):
      filename = "Idle__00{}.png".format(i)
      img = pg.image.load(os.path.join(img_folder, filename))
      img = pg.transform.scale(img, (int(img.get_width()/3),int(img.get_height()/3)))
      self.idle_anim_R.append(img)
      img = pg.transform.flip(img, 1,0)
      self.idle_anim_L.append(img)

    for i in range(9):
      filename = "Run__00{}.png".format(i)
      img = pg.image.load(os.path.join(img_folder, filename))
      img = pg.transform.scale(img, (int(img.get_width()/3),int(img.get_height()/3)))
      self.run_anim_R.append(img)
      img = pg.transform.flip(img, 1,0)
      self.run_anim_L.append(img)

    for i in range(9):
      filename = "Dead__00{}.png".format(i)
      img = pg.image.load(os.path.join(img_folder, filename))
      img = pg.transform.scale(img, (int(img.get_width()/3),int(img.get_height()/3)))
      self.dead_anim_R.append(img)
      img = pg.transform.flip(img, 1,0)
      self.dead_anim_L.append(img)

    for i in range(9):
      filename = "Attack__00{}.png".format(i)
      img = pg.image.load(os.path.join(img_folder, filename))
      img = pg.transform.scale(img, (int(img.get_width()/3),int(img.get_height()/3)))
      self.attack_anim_R.append(img)
      img = pg.transform.flip(img, 1,0)
      self.attack_anim_L.append(img)



  def moveX(self,input):
      if abs(self.speedX) < MAXSPEED: self.speedX -= input*4

  def moveY(self,input):
      if abs(self.speedY) < MAXSPEED: self.speedY -= input*2
      

  def update(self):

    # apply friction 
    self.speedX = self.speedX*FRICTION
    self.speedY = self.speedY*FRICTION
    
    # stop if slow
    if abs(self.speedX) < .08:
      self.speedX = 0
    else:
      # only change $facing if fast
      self.facingR = int(self.speedX+1)
    if abs(self.speedY) < .08:
      self.speedY = 0
    if abs(self.speedX)+abs(self.speedY) < .16:
      self.isWalking = 0
    else:
      self.isWalking = 1

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


    frame = int((pg.time.get_ticks()-self.start_ticks)/100)%9

    if self.subClassAnimation == 0:
      if self.isDead:
        if self.facingR > 0:
          self.image = self.dead_anim_R[8]
        else:
          self.image = self.dead_anim_L[8]

      elif self.isDying:
        if self.facingR > 0:
          self.image = self.dead_anim_R[frame]
        else:
          self.image = self.dead_anim_L[frame]
        if frame == 8:
          self.isDead = 1
          self.isDying = 0

      elif self.isAttacking:
        if self.facingR > 0:
          self.image = self.attack_anim_R[frame]
        else:
          self.image = self.attack_anim_L[frame]
        if frame >= 8:
          self.isAttacking = 0

      elif self.isWalking:
        if self.facingR > 0:
          self.image = self.run_anim_R[frame]
        else:
          self.image = self.run_anim_L[frame]

      else:
        if self.facingR > 0:
          self.image = self.idle_anim_R[frame]
        else:
          self.image = self.idle_anim_L[frame]


    # draw new postion
    #self.rect = ( int(self.posX), int(self.posY),
     #             self.rect[2], self.rect[3])
    self.rect = ( int(self.posX-self.image.get_width()/2),
                  int(self.posY-self.image.get_height()),
                #  self.rect[2], self.rect[3])
                  self.image.get_width(),
                  self.image.get_height())

  #  self.reload += 1
  #  if self.isShooting and self.reload >= 10:
  #      self.reload = 0
  #      self.isShooting = 0
  #      return ['Bomb',int(self.posX), int(self.posY),self.speedX,self.speedY]
  #  self.isShooting = 0

    return [0]


  def takeHit(self):
    pass

    
  def die(self):
    print('Im dead')
    return ['GAMEOVER',int(self.posX), int(self.posY),self.speedX,self.speedY]


